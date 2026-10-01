"""Shared helpers for scripts that render branded images (square logo, hero
section, ...) straight from properdocs.yml."""

import io
import re
import subprocess
from pathlib import Path

import cairosvg
from PIL import Image, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = REPO_ROOT / "properdocs.yml"

# properdocs.yml pulls in custom YAML tags (!ENV, !!python/name:...) from
# various plugins, which a plain PyYAML loader doesn't know about. Rather
# than registering every tag, just regex out the values we need.


def load_config(config_path: Path = DEFAULT_CONFIG) -> str:
    return config_path.read_text()


def get_icon_path(config_text: str) -> str:
    m = re.search(r"theme:.*?icon:.*?logo:\s*(\S+)", config_text, re.DOTALL)
    if not m:
        raise ValueError("theme.icon.logo not found in config")
    return m.group(1)


def get_light_primary(config_text: str) -> str:
    m = re.search(r'palette:\s*\n(.*?)(?=\n\S|\Z)', config_text, re.DOTALL)
    if not m:
        raise ValueError("theme.palette not found in config")
    palette_block = m.group(1)
    entries = re.split(r"\n\s*-\s*", palette_block)
    for entry in entries:
        if "light" in entry or re.search(r"scheme:\s*default", entry):
            pm = re.search(r"primary:\s*['\"]?([\w-]+)['\"]?", entry)
            if pm:
                return pm.group(1)
    raise ValueError("light palette entry with a primary color not found")


def get_site_name(config_text: str) -> str | None:
    m = re.search(r'^site_name:\s*["\']?(.*?)["\']?\s*$', config_text, re.MULTILINE)
    return m.group(1) if m else None


def get_site_author(config_text: str) -> str | None:
    m = re.search(r'^site_author:\s*["\']?(.*?)["\']?\s*$', config_text, re.MULTILINE)
    return m.group(1) if m else None


def get_site_email(config_text: str) -> str | None:
    m = re.search(r'^site_email:\s*["\']?(.*?)["\']?\s*$', config_text, re.MULTILINE)
    return m.group(1) if m else None


def find_bold_font(size: int) -> ImageFont.FreeTypeFont:
    try:
        path = subprocess.check_output(
            ["fc-match", "-f", "%{file}", "sans-serif:bold"], text=True
        ).strip()
        font = ImageFont.truetype(path, size)
        try:
            font.set_variation_by_axes([700])  # variable fonts: force bold weight
        except Exception:
            pass
        return font
    except Exception:
        return ImageFont.load_default(size=size)


def find_regular_font(size: int) -> ImageFont.FreeTypeFont:
    try:
        path = subprocess.check_output(
            ["fc-match", "-f", "%{file}", "sans-serif"], text=True
        ).strip()
        font = ImageFont.truetype(path, size)
        try:
            font.set_variation_by_axes([400])
        except Exception:
            pass
        return font
    except Exception:
        return ImageFont.load_default(size=size)


def find_icon_svg(icon_path: str) -> Path:
    import material
    import material_joapuiib

    search_dirs = [
        Path(material_joapuiib.__file__).resolve().parent / "templates" / ".icons",
        Path(material.__file__).resolve().parent / "templates" / ".icons",
    ]
    for d in search_dirs:
        candidate = d / f"{icon_path}.svg"
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"Icon not found: {icon_path}")


def find_palette_css() -> Path:
    import material

    stylesheets = Path(material.__file__).resolve().parent / "templates" / "assets" / "stylesheets"
    matches = sorted(stylesheets.glob("palette.*.min.css"))
    if not matches:
        raise FileNotFoundError("palette css not found")
    return matches[0]


def get_primary_colors(primary_name: str) -> tuple[str, str]:
    """Returns (background, icon_color) for a named Material primary color."""
    css = find_palette_css().read_text()
    # Material splits each [data-md-color-primary=X] selector across several
    # separate rule bodies (one per declared property group) — merge them all.
    bodies = re.findall(r"\[data-md-color-primary=%s\]\{([^}]*)\}" % re.escape(primary_name), css)
    if not bodies:
        raise ValueError(f"Primary color {primary_name!r} not found in palette css")
    combined = "".join(bodies)
    fg_m = re.search(r"--md-primary-fg-color:([^;]+);", combined)
    bg_m = re.search(r"--md-primary-bg-color:([^;]+);", combined)
    if not fg_m or not bg_m:
        raise ValueError(f"Primary color {primary_name!r} is missing fg/bg color vars")
    return fg_m.group(1), bg_m.group(1)


def svg_view_box(svg_text: str) -> tuple[float, float]:
    m = re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+) ([\d.]+)"', svg_text)
    w, h = float(m.group(1)), float(m.group(2))
    return w, h


def render_icon_png(svg_path: Path, color: str, width: float, height: float) -> Image.Image:
    svg_text = svg_path.read_text()
    svg_text = svg_text.replace("<svg ", f'<svg fill="{color}" ', 1)
    png_bytes = cairosvg.svg2png(bytestring=svg_text.encode(), output_width=round(width), output_height=round(height))
    return Image.open(io.BytesIO(png_bytes)).convert("RGBA")


def find_main_css() -> Path:
    import material

    stylesheets = Path(material.__file__).resolve().parent / "templates" / "assets" / "stylesheets"
    matches = sorted(stylesheets.glob("main.*.min.css"))
    if not matches:
        raise FileNotFoundError("main css not found")
    return matches[0]


def parse_color(css_color: str) -> tuple[int, int, int, float]:
    """Parse a CSS hex color (#rgb, #rgba, #rrggbb or #rrggbbaa) into (r, g, b, alpha)."""
    hexs = css_color.strip().lstrip("#")
    if len(hexs) in (3, 4):
        hexs = "".join(c * 2 for c in hexs)
    if len(hexs) not in (6, 8):
        raise ValueError(f"Unsupported color format: {css_color!r}")
    r, g, b = (int(hexs[i:i + 2], 16) for i in (0, 2, 4))
    a = int(hexs[6:8], 16) / 255 if len(hexs) == 8 else 1.0
    return r, g, b, a


def blend_over(fg: tuple[int, int, int, float], bg: tuple[int, int, int]) -> tuple[int, int, int]:
    r, g, b, a = fg
    return tuple(round(c * a + base * (1 - a)) for c, base in zip((r, g, b), bg))


def get_default_text_colors(bg: tuple[int, int, int] = (255, 255, 255)) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    """Returns (title_color, muted_color): Material's default (scheme-independent)
    text colors, flattened as opaque RGB over the given background."""
    css = find_main_css().read_text()
    fg_m = re.search(r"--md-default-fg-color:([^;]+);", css)
    fg_light_m = re.search(r"--md-default-fg-color--light:([^;]+);", css)
    if not fg_m or not fg_light_m:
        raise ValueError("default text colors not found in main css")
    title_color = blend_over(parse_color(fg_m.group(1)), bg)
    muted_color = blend_over(parse_color(fg_light_m.group(1)), bg)
    return title_color, muted_color


def git_config_value(key: str) -> str | None:
    try:
        return subprocess.check_output(["git", "config", key], text=True, cwd=REPO_ROOT).strip() or None
    except Exception:
        return None
