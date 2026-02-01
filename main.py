#!/usr/bin/env python3
"""
Pillow verification script.
Tests basic image processing functionality.
"""

from PIL import Image
import os

# Create test image
print("Creating 100x100 RGB image...")
img = Image.new('RGB', (100, 100), color='blue')

# Save as PNG
print("Saving as PNG...")
img.save('/app/test_image.png')

# Load back
print("Loading image back...")
img2 = Image.open('/app/test_image.png')
assert img2.format == 'PNG',f"Format mismatch, expected PNG but got: {img2.format}"

# Test JPEG support
print("Testing JPEG support...")
img_jpeg = Image.new('RGB', (100, 100), color='red')
img_jpeg.save('/app/test_image.jpg', 'JPEG')
img_jpeg2 = Image.open('/app/test_image.jpg')
assert img_jpeg2.format == 'JPEG', f"Format mismatch, expected JPEG but got:{img_jpeg2.format}"

print("\nSuccess: Pillow is working correctly")
print("PNG support: OK")
print("JPEG support: OK")