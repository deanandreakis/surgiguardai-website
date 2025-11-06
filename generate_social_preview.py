#!/usr/bin/env python3
"""
Generate social media preview image for SurgiGuard AI
Standard size: 1200x630 for optimal display on all platforms
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_social_preview():
    """Create a 1200x630 social media preview image"""

    # Standard social media image size
    width = 1200
    height = 630

    # Create image with gradient background
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Create gradient background (blue gradient)
    for y in range(height):
        # Gradient from #0066cc to #004c99
        ratio = y / height
        r = int(0 + (0 - 0) * ratio)
        g = int(102 - (102 - 76) * ratio)
        b = int(204 - (204 - 153) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Try to use a system font, fall back to default if not available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
        tagline_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except:
        # Fallback to default font with size parameter
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        tagline_font = ImageFont.load_default()

    # Add brand name
    brand_text = "SurgiGuard AI"

    # Calculate text position for centering
    # Using textbbox instead of deprecated textsize
    bbox = draw.textbbox((0, 0), brand_text, font=title_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) / 2
    y = 120

    # Draw brand name with shadow effect
    shadow_offset = 3
    draw.text((x + shadow_offset, y + shadow_offset), brand_text, fill=(0, 0, 0, 128), font=title_font)
    draw.text((x, y), brand_text, fill=(255, 255, 255), font=title_font)

    # Add main tagline
    tagline = "Surgical Instrument Tracking"
    bbox = draw.textbbox((0, 0), tagline, font=subtitle_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    y = 240
    draw.text((x, y), tagline, fill=(0, 204, 136), font=subtitle_font)

    tagline2 = "& Count Verification"
    bbox = draw.textbbox((0, 0), tagline2, font=subtitle_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    y = 290
    draw.text((x, y), tagline2, fill=(0, 204, 136), font=subtitle_font)

    # Add description
    description = "AI-Powered Computer Vision to Prevent"
    bbox = draw.textbbox((0, 0), description, font=tagline_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    y = 380
    draw.text((x, y), description, fill=(255, 255, 255, 230), font=tagline_font)

    description2 = "Retained Surgical Items"
    bbox = draw.textbbox((0, 0), description2, font=tagline_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    y = 425
    draw.text((x, y), description2, fill=(255, 255, 255, 230), font=tagline_font)

    # Add decorative elements (medical cross icon)
    # Small medical cross in top left
    cross_size = 40
    cross_width = 12
    cross_x = 60
    cross_y = 60

    # Vertical bar
    draw.rectangle(
        [(cross_x - cross_width//2, cross_y - cross_size//2),
         (cross_x + cross_width//2, cross_y + cross_size//2)],
        fill=(255, 255, 255, 200)
    )

    # Horizontal bar
    draw.rectangle(
        [(cross_x - cross_size//2, cross_y - cross_width//2),
         (cross_x + cross_size//2, cross_y + cross_width//2)],
        fill=(255, 255, 255, 200)
    )

    # Add tech corner accents
    accent_color = (0, 204, 136)
    corner_size = 8

    # Top right corner
    positions = [(width - 80, 60), (width - 140, 60), (width - 80, 120), (width - 140, 120)]

    for pos_x, pos_y in positions:
        draw.ellipse(
            [(pos_x - corner_size, pos_y - corner_size),
             (pos_x + corner_size, pos_y + corner_size)],
            fill=accent_color
        )

    # Draw connecting lines
    draw.line([(width - 80, 60), (width - 140, 120)], fill=accent_color, width=2)
    draw.line([(width - 140, 60), (width - 80, 120)], fill=accent_color, width=2)

    # Add stats at bottom
    stats_y = 510
    stats = [
        ("5,500+", "Annual RSI Cases"),
        ("$200K", "Avg Cost/Incident"),
        ("99.9%", "Accuracy Rate")
    ]

    stat_spacing = width // 3

    for i, (number, label) in enumerate(stats):
        # Position for each stat
        stat_x = stat_spacing * i + stat_spacing // 2

        # Draw number
        bbox = draw.textbbox((0, 0), number, font=subtitle_font)
        num_width = bbox[2] - bbox[0]
        draw.text((stat_x - num_width//2, stats_y), number, fill=(0, 204, 136), font=subtitle_font)

        # Draw label
        bbox = draw.textbbox((0, 0), label, font=tagline_font)
        label_width = bbox[2] - bbox[0]
        draw.text((stat_x - label_width//2, stats_y + 45), label, fill=(255, 255, 255, 200), font=tagline_font)

    # Save the image
    img.save('social-preview.png', 'PNG', optimize=True, quality=95)
    print(f"Created social-preview.png (1200x630)")
    print("This image is optimized for:")
    print("  - Facebook/Meta Open Graph")
    print("  - Twitter/X Cards")
    print("  - LinkedIn")
    print("  - Discord embeds")
    print("  - Other social platforms")

if __name__ == '__main__':
    create_social_preview()
