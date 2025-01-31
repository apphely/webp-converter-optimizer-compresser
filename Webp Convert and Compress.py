from PIL import Image
import os

# Define the input folder
folder_path = 'X:\Webp'

# Get all files in the folder
file_list = os.listdir(folder_path)

for file_name in file_list:
    if file_name.endswith(('.jpg', '.jpeg', '.png')):
        # Create the path to the input file
        input_path = os.path.join(folder_path, file_name)
        
        # Upload image and convert to webp
        im = Image.open(input_path)
        webp_path = os.path.splitext(input_path)[0] + '.webp'
        im.save(webp_path, 'WEBP', quality=5)  #Set the Quality

print("All photos were converted to webp format and saved in the same folder.")