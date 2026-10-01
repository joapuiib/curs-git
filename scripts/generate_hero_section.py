#!/usr/bin/env python3
"""Render a wide hero-section banner (site icon + title + author), styled
after the site's landing-page hero (transparent background by default, blurred
primary-color blobs, small uppercase eyebrow, bold title, muted subtitle),
read straight from properdocs.yml. Meant to be dropped at the top of a Moodle
course page."""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from site_assets import (
    DEFAULT_CONFIG,
    REPO_ROOT,
    find_bold_font,
    find_icon_svg,
    find_regular_font,
    get_default_text_colors,
    get_icon_path,
    get_light_primary,
    get_primary_colors,
    get_site_author,
    get_site_email,
    get_site_name,
    git_config_value,
    load_config,
    parse_color,
    render_icon_png,
    svg_view_box,
)


def default_name() -> str | None:
    return git_config_value("user.name")


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_width: float, size: int, min_size: int, bold: bool):
    make_font = find_bold_font if bold else find_regular_font
    font = make_font(size)
    while size > min_size:
        bbox = draw.textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= max_width:
            break
        size -= 1
        font = make_font(size)
    return font


def draw_blobs(width: int, height: int, color: tuple[int, int, int], opacity: float) -> Image.Image:
    """Two large, blurred, low-opacity circles behind the hero content,
    echoing the landing page's decorative gradient blob."""
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    alpha = round(255 * opacity)
    radius = round(height * 0.75)
    for cx_frac, cy_frac in ((0.28, 0.25), (0.78, 0.75)):
        cx, cy = width * cx_frac, height * cy_frac
        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=(*color, alpha))
    return layer.filter(ImageFilter.GaussianBlur(radius=height * 0.18))


def generate_hero_section(
    icon_path: str,
    accent_color: str,
    bg_color: tuple[int, int, int] | None,
    title_color: tuple[int, int, int],
    muted_color: tuple[int, int, int],
    output: Path,
    width: int,
    height: int,
    title: str,
    author: str | None,
    eyebrow: str | None = None,
    padding: float = 0.14,
    title_size: float = 0.22,
    eyebrow_size: float = 0.075,
    author_size: float = 0.1,
    block_gap: float = 0.05,
) -> None:
    pad_x = pad_y = round(height * padding)
    max_w = width - 2 * pad_x

    canvas = Image.new("RGBA", (width, height), (*bg_color, 255) if bg_color else (0, 0, 0, 0))
    canvas = Image.alpha_composite(canvas, draw_blobs(width, height, parse_color(accent_color)[:3], opacity=0.28))
    draw = ImageDraw.Draw(canvas)

    gap_px = round(height * block_gap)

    eyebrow_font = eyebrow_bbox = eyebrow_h = None
    if eyebrow:
        eyebrow = eyebrow.upper()
        eyebrow_font = fit_font(draw, eyebrow, max_w, round(height * eyebrow_size), round(height * 0.04), bold=True)
        eyebrow_bbox = draw.textbbox((0, 0), eyebrow, font=eyebrow_font)
        eyebrow_h = eyebrow_bbox[3] - eyebrow_bbox[1]

    title_h_px = round(height * title_size)
    icon_h = round(title_h_px * 1.15)
    svg_path = find_icon_svg(icon_path)
    view_w, view_h = svg_view_box(svg_path.read_text())
    icon_w = icon_h * (view_w / view_h)
    icon_gap = round(height * 0.035)

    title_font = fit_font(draw, title, max_w - icon_w - icon_gap, title_h_px, round(height * 0.08), bold=True)
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    title_h = title_bbox[3] - title_bbox[1]
    title_row_w = icon_w + icon_gap + title_w
    title_row_h = max(icon_h, title_h)

    icon = render_icon_png(svg_path, "#%02x%02x%02x" % title_color, icon_w, icon_h)

    author_font = author_bbox = author_h = None
    if author:
        author_font = fit_font(draw, author, max_w, round(height * author_size), round(height * 0.05), bold=False)
        author_bbox = draw.textbbox((0, 0), author, font=author_font)
        author_h = author_bbox[3] - author_bbox[1]

    content_h = title_row_h
    if eyebrow:
        content_h += gap_px + eyebrow_h
    if author:
        content_h += gap_px + author_h

    top = max(pad_y, (height - content_h) / 2)
    cx = width / 2

    y = top
    if eyebrow:
        draw.text((cx - (eyebrow_bbox[2] - eyebrow_bbox[0]) / 2 - eyebrow_bbox[0], y - eyebrow_bbox[1]), eyebrow, font=eyebrow_font, fill=accent_color)
        y += eyebrow_h + gap_px

    row_x = cx - title_row_w / 2
    icon_y = round(y + (title_row_h - icon_h) / 2)
    canvas.paste(icon, (round(row_x), icon_y), icon)
    title_x = row_x + icon_w + icon_gap
    draw.text((title_x - title_bbox[0], y + (title_row_h - title_h) / 2 - title_bbox[1]), title, font=title_font, fill=title_color)
    y += title_row_h

    if author:
        y += gap_px
        draw.text((cx - (author_bbox[2] - author_bbox[0]) / 2 - author_bbox[0], y - author_bbox[1]), author, font=author_font, fill=muted_color)

    output.parent.mkdir(parents=True, exist_ok=True)
    (canvas if bg_color is None else canvas.convert("RGB")).save(output)
    print(f"Saved {width}x{height} hero section ({icon_path}) to {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="Path to properdocs.yml")
    parser.add_argument("--icon", default=None, help="Icon path override (default: theme.icon.logo)")
    parser.add_argument("--primary", default=None, help="Primary color name override (default: light palette's primary)")
    parser.add_argument("--accent-color", default=None, help="Eyebrow/blob accent color override (default: primary color)")
    parser.add_argument("--bg-color", default=None, help="Background color (default: transparent); pass a CSS hex color for an opaque background")
    parser.add_argument("--output", type=Path, default=REPO_ROOT / "site/hero.png", help="Output PNG path")
    parser.add_argument("--width", type=int, default=1200, help="Banner width in pixels")
    parser.add_argument("--height", type=int, default=300, help="Banner height in pixels")
    parser.add_argument("--title", default=None, help="Title text (default: site_name)")
    parser.add_argument("--eyebrow", default=None, help="Small uppercase label above the title (default: none)")
    parser.add_argument("--name", default=None, help="Author name (default: git user.name)")
    parser.add_argument("--email", default=None, help="Author email override (default: site_email config, falling back to git user.email)")
    parser.add_argument("--padding", type=float, default=0.14, help="Padding as a fraction of the banner height")
    args = parser.parse_args()

    config = load_config(args.config)
    icon_path = args.icon or get_icon_path(config)
    primary = args.primary or get_light_primary(config)
    accent_color, _ = get_primary_colors(primary)
    title = args.title or get_site_name(config) or ""

    name = args.name if args.name is not None else default_name()
    email = args.email if args.email is not None else (get_site_email(config) or git_config_value("user.email"))
    author = " · ".join(part for part in (name, email) if part) or get_site_author(config)

    bg_color = parse_color(args.bg_color)[:3] if args.bg_color else None
    title_color, muted_color = get_default_text_colors(bg=bg_color or (255, 255, 255))

    generate_hero_section(
        icon_path=icon_path,
        accent_color=args.accent_color or accent_color,
        bg_color=bg_color,
        title_color=title_color,
        muted_color=muted_color,
        output=args.output,
        width=args.width,
        height=args.height,
        title=title,
        author=author or None,
        eyebrow=args.eyebrow,
        padding=args.padding,
    )


if __name__ == "__main__":
    main()
