#!/usr/bin/env python3
"""Render the site's icon (theme.icon.logo) as a square PNG, using the
primary color of the site's light palette as background, read straight
from properdocs.yml."""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw

from site_assets import (
    DEFAULT_CONFIG,
    REPO_ROOT,
    find_bold_font,
    find_icon_svg,
    get_icon_path,
    get_light_primary,
    get_primary_colors,
    get_site_name,
    load_config,
    render_icon_png,
    svg_view_box,
)


def generate_square_logo(
    icon_path: str,
    bg_color: str,
    icon_color: str,
    output: Path,
    padding: float,
    side: int,
    text: str | None = None,
    font_size: float = 0.09,
    gap: float = 0.04,
) -> None:
    svg_path = find_icon_svg(icon_path)
    view_w, view_h = svg_view_box(svg_path.read_text())
    aspect = view_w / view_h

    inner = side * (1 - 2 * padding)
    text_h = side * font_size if text else 0
    gap_px = side * gap if text else 0
    icon_budget = inner - text_h - gap_px

    if aspect >= 1:
        icon_w, icon_h = icon_budget, icon_budget / aspect
    else:
        icon_w, icon_h = icon_budget * aspect, icon_budget

    icon = render_icon_png(svg_path, icon_color, icon_w, icon_h)

    canvas = Image.new("RGB", (side, side), bg_color)
    draw = ImageDraw.Draw(canvas)

    font = find_bold_font(round(text_h)) if text else None
    text_bbox = draw.textbbox((0, 0), text, font=font) if text else (0, 0, 0, 0)
    text_w = text_bbox[2] - text_bbox[0]

    content_h = icon.height + (gap_px + text_h if text else 0)
    top = (side - content_h) / 2

    icon_x = round((side - icon.width) / 2)
    icon_y = round(top)
    canvas.paste(icon, (icon_x, icon_y), icon)

    if text:
        text_x = round((side - text_w) / 2 - text_bbox[0])
        text_y = round(top + icon.height + gap_px - text_bbox[1])
        draw.text((text_x, text_y), text, font=font, fill=icon_color)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)
    print(f"Saved {side}x{side} square logo ({icon_path}, bg {bg_color}) to {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="Path to properdocs.yml")
    parser.add_argument("--icon", default=None, help="Icon path override (default: theme.icon.logo)")
    parser.add_argument("--primary", default=None, help="Primary color name override (default: light palette's primary)")
    parser.add_argument("--bg-color", default=None, help="Background color override")
    parser.add_argument("--icon-color", default=None, help="Icon fill color override")
    parser.add_argument("--output", type=Path, default=REPO_ROOT / "site/logo.png", help="Output PNG path")
    parser.add_argument("--padding", type=float, default=0.22, help="Padding around the icon (+ text) as a fraction of the square side")
    parser.add_argument("--size", type=int, default=512, help="Square side in pixels")
    parser.add_argument("--text", default=None, help="Text below the icon (default: site_name; pass '' for none)")
    parser.add_argument("--font-size", type=float, default=0.09, help="Text height as a fraction of the square side")
    parser.add_argument("--gap", type=float, default=0.04, help="Gap between icon and text as a fraction of the square side")
    args = parser.parse_args()

    config = load_config(args.config)
    icon_path = args.icon or get_icon_path(config)
    primary = args.primary or get_light_primary(config)
    fg_color, icon_color = get_primary_colors(primary)
    text = args.text if args.text is not None else get_site_name(config)

    generate_square_logo(
        icon_path=icon_path,
        bg_color=args.bg_color or fg_color,
        icon_color=args.icon_color or icon_color,
        output=args.output,
        padding=args.padding,
        side=args.size,
        text=text or None,
        font_size=args.font_size,
        gap=args.gap,
    )


if __name__ == "__main__":
    main()
