from PIL import Image
import os
import shutil

def compress_images(folder_path, output_folder, quality_thresholds):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files and subfolders in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Check if the file is an image
            if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                # Get the size of the image
                image_size = os.path.getsize(file_path)

                # Iterate over the quality thresholds and compress accordingly
                for threshold, quality in quality_thresholds.items():
                    if image_size > threshold:
                        # Open the image using Pillow
                        image = Image.open(file_path)

                        # Compress the image with the specified quality
                        compressed_image = image.copy()
                        compressed_image.save(file_path, optimize=True, quality=quality)

                        # Close the images
                        image.close()
                        compressed_image.close()

                        # Get the parent folder name
                        parent_folder_name = os.path.basename(os.path.dirname(file_path))

                        # Create the destination folder based on the parent folder name
                        destination_folder = os.path.join(output_folder, parent_folder_name)
                        os.makedirs(destination_folder, exist_ok=True)

                        # Copy the compressed image to the destination folder
                        destination_path = os.path.join(destination_folder, file_name)
                        shutil.move(file_path, destination_path)

# Specify the folder containing the images
folder_path = 'data\Plant Disease\Plants Disease Dataset Subset\Cauliflower/valid'

# Specify the output folder where compressed images will be saved
output_folder = folder_path

# Specify the size thresholds and corresponding quality levels
quality_thresholds = {
    5e5: 20,   # Quality 80 for images larger than 1MB
}

# Call the function to compress and copy the images
compress_images(folder_path, output_folder, quality_thresholds)
