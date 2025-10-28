#!/usr/bin/env python3
"""
Generate placeholder images for the academic website.
This creates basic placeholder images so you can test the website immediately.
Replace these with your actual images later.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

def create_placeholder_image(filename, size, text, bg_color, text_color='white'):
    """Create a placeholder image with text"""
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a basic font, fallback to default if not available
    try:
        font_size = min(size[0], size[1]) // 10
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position to center text
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    # Draw text
    draw.text(position, text, fill=text_color, font=font)
    
    # Save image
    img.save(f'images/{filename}')
    print(f"Created: images/{filename}")

# Create placeholder images
print("Generating placeholder images...")

# Profile photo (square)
create_placeholder_image(
    'profile.jpg',
    (400, 400),
    'Your\nPhoto\nHere',
    '#2c3e50'
)

# AstroDiff before (blurry/turbulent)
img_before = Image.new('RGB', (160, 160), color='#1a1a2e')
draw = ImageDraw.Draw(img_before)
# Add some blur effect simulation with gradients
for i in range(20):
    alpha = 255 - i * 10
    color = (30 + i*5, 30 + i*5, 50 + i*5)
    draw.ellipse([30+i, 30+i, 130-i, 130-i], fill=color)
draw.text((50, 70), "Blurry", fill='#888888')
img_before.save('images/astrodiff_before.jpg')
print("Created: images/astrodiff_before.jpg")

# AstroDiff after (clear)
img_after = Image.new('RGB', (160, 160), color='#0f0f1e')
draw = ImageDraw.Draw(img_after)
# Add stars
import random
random.seed(42)
for _ in range(50):
    x, y = random.randint(0, 160), random.randint(0, 160)
    size = random.choice([1, 1, 1, 2])
    if size == 1:
        draw.point((x, y), fill='white')
    else:
        draw.ellipse([x, y, x+size, y+size], fill='white')
# Add a bright star/galaxy
draw.ellipse([70, 70, 90, 90], fill='#ffffff')
draw.text((55, 130), "Clear", fill='white')
img_after.save('images/astrodiff_after.jpg')
print("Created: images/astrodiff_after.jpg")

# TSD-SR paper image (aerial view)
create_placeholder_image(
    'tsdsr.jpg',
    (160, 160),
    'Aerial\nImage',
    '#4a7c59',
    'white'
)

# Institution logo
logo = Image.new('RGBA', (160, 60), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(logo)
draw.rectangle([0, 0, 159, 59], fill='#c5b783', outline='#8e7f5b', width=2)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
except:
    font = ImageFont.load_default()
draw.text((20, 20), "PURDUE", fill='black', font=font)
logo.save('images/purdue_logo.png')
print("Created: images/purdue_logo.png")

print("\n✅ All placeholder images created successfully!")
print("\nNext steps:")
print("1. Replace these placeholder images with your actual images")
print("2. Update the HTML with your information")
print("3. Deploy to your preferred hosting platform")
print("\nImage requirements:")
print("- profile.jpg: Your professional photo (square, ~400x400px or larger)")
print("- astrodiff_before.jpg: Turbulent astronomical image (160x160px)")
print("- astrodiff_after.jpg: Restored astronomical image (160x160px)")
print("- tsdsr.jpg: Aerial image sample (160x160px)")
print("- purdue_logo.png: Your institution logo (160x60px)")
