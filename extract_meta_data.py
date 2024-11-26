from PIL import Image
from PIL.ExifTags import TAGS

# Open image
img = Image.open("d5eead80-c48c-4bcf-86c0-c3e65d10909c.JPG")
exif_data = img._getexif()

# Translate EXIF tags into human-readable form
if exif_data:
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        print(f"{tag_name}: {value}")
else:
    print("No EXIF data found.")
