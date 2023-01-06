import os
from PIL import Image

# Define the path of the folder we want to scan
path = "/Users/joseeduardonunezarenas/Desktop/Imagenes"

# Iterate through the files in the folder
for file in os.listdir(path):
  # If the file is an image
  if file.endswith(".jpg") or file.endswith(".png"):
    # Open the image with PIL
    with Image.open(os.path.join(path, file)) as im:
      # Reduce the quality of the image to 50%
      im.save(os.path.join(path, file), quality=10)
