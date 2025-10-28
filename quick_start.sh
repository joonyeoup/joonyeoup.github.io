#!/bin/bash
# Quick Start Script for Academic Portfolio Website

echo "========================================="
echo "Academic Portfolio Website - Quick Start"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Generate placeholder images if they don't exist
if [ ! -d "images" ] || [ -z "$(ls -A images)" ]; then
    echo "📸 Generating placeholder images..."
    pip install Pillow --quiet 2>/dev/null || pip3 install Pillow --quiet 2>/dev/null
    python3 generate_placeholders.py
    echo ""
fi

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit index.html with your information"
echo "2. Replace placeholder images in the images/ folder"
echo "3. Preview locally by running: python3 preview_server.py"
echo "4. Deploy to GitHub Pages, Netlify, or your preferred host"
echo ""
echo "To preview now, run:"
echo "  python3 preview_server.py"
echo ""
echo "For deployment instructions, see README.md"
echo "========================================="
