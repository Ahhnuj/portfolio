from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a size of 32x32 pixels
img = Image.new('RGB', (32, 32), color='#0d6efd')
d = ImageDraw.Draw(img)

# Add text
text = "AT"
# Use a default font since custom fonts might not be available
d.text((8, 8), text, fill='white')

# Ensure the directory exists
os.makedirs('static/images', exist_ok=True)

# Save the image as ICO
img.save('static/images/favicon.ico') 