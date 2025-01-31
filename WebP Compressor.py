from PIL import Image
import os

# List all files in the folder
folder_path = "x:\Webp"  # Path to the folder with the webp files
c_quality = 25 #Quality

# Get all files in a folder
files = os.listdir(folder_path)

# Process Webp Files
for dosya_adı in files:
    if dosya_adı.endswith(".webp"):
        file_path = os.path.join(folder_path, dosya_adı)

        # Open Webp File
        im = Image.open(file_path)

        # Set quality and save
        im.save(file_path, "webp", quality=c_quality)

print("Webp filesı %15 kalitesinde sıkıştırıldı.")
