from rembg import remove
from PIL import Image
import os

# Define input and output paths
input_path = '/home/parallels/Documents/Dev/input_image_.jpeg'
output_path = '/home/parallels/Documents/Dev/output/input_image_.png'
output_folder = '/home/parallels/Documents/Dev/output/'

# Get a list of all files in the folder
file_list = os.listdir(output_folder)

# Loop through the files and remove them one by one
for file_name in file_list:
    file_path = os.path.join(output_folder, file_name)
    os.remove(file_path)
    print(f"Deleted file: {file_name}")

print("All files in the folder have been deleted.")


# Loop over the images
for i in range(1, 40):
	#Construct the source and destination file paths
	source_file = f"{input_path[:-5]}{i}.jpeg"
	destination_file = f"{output_path[:-4]}{i}.png"

	print(source_file)
	print(destination_file)

	# Open the input image
	input_image = Image.open(source_file)

	# Remove the background
	output_image = remove(input_image)

	# Save the processed image
	output_image.save(destination_file)