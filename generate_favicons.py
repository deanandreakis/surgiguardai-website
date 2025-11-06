#!/usr/bin/env python3
"""
Generate PNG favicons from design specifications for SurgiGuard AI
"""

from PIL import Image, ImageDraw
import math

def create_favicon(size, output_file):
    """Create a favicon with the SurgiGuard AI design"""

    # Create image with transparency
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    scale = size / 64

    # Draw gradient circle background (approximating with solid color for simplicity)
    # In production, you'd want a proper gradient
    circle_color = (0, 102, 204)  # Primary blue color
    center = size / 2
    radius = (size / 2) - scale

    # Draw circle
    draw.ellipse(
        [(center - radius, center - radius),
         (center + radius, center + radius)],
        fill=circle_color
    )

    # Draw medical cross (white)
    cross_width = int(8 * scale)
    cross_height = int(28 * scale)

    # Vertical bar
    vert_x = int((size - cross_width) / 2)
    vert_y = int(18 * scale)
    draw.rectangle(
        [(vert_x, vert_y),
         (vert_x + cross_width, vert_y + cross_height)],
        fill=(255, 255, 255)
    )

    # Horizontal bar
    horz_x = int(18 * scale)
    horz_y = int((size - cross_width) / 2)
    draw.rectangle(
        [(horz_x, horz_y),
         (horz_x + cross_height, horz_y + cross_width)],
        fill=(255, 255, 255)
    )

    # Draw AI/Tech corner accents
    dot_radius = int(2 * scale)
    dot_offset = int(20 * scale)
    dot_offset2 = int(44 * scale)
    accent_color = (0, 204, 136)  # Secondary green color

    # Corner dots
    positions = [
        (dot_offset, dot_offset),
        (dot_offset2, dot_offset),
        (dot_offset, dot_offset2),
        (dot_offset2, dot_offset2)
    ]

    for x, y in positions:
        draw.ellipse(
            [(x - dot_radius, y - dot_radius),
             (x + dot_radius, y + dot_radius)],
            fill=accent_color
        )

    # Draw connecting lines
    line_width = max(1, int(scale))
    line_color = (0, 204, 136, 153)  # Semi-transparent green

    # Create a new layer for lines with transparency
    line_layer = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    line_draw = ImageDraw.Draw(line_layer)

    connections = [
        (dot_offset, dot_offset, int(26 * scale), int(26 * scale)),
        (dot_offset2, dot_offset, int(38 * scale), int(26 * scale)),
        (dot_offset, dot_offset2, int(26 * scale), int(38 * scale)),
        (dot_offset2, dot_offset2, int(38 * scale), int(38 * scale))
    ]

    for x1, y1, x2, y2 in connections:
        line_draw.line([(x1, y1), (x2, y2)], fill=line_color, width=line_width)

    # Composite the line layer onto the main image
    img = Image.alpha_composite(img, line_layer)

    # Save the image
    img.save(output_file, 'PNG')
    print(f"Created {output_file} ({size}x{size})")

if __name__ == '__main__':
    # Generate 32x32 favicon
    create_favicon(32, 'favicon-32x32.png')

    # Generate 180x180 Apple Touch Icon
    create_favicon(180, 'apple-touch-icon.png')

    print("Favicon generation complete!")
