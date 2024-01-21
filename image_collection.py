import os

def get_image_paths(folder_path, extensions=('jpg', 'jpeg', 'png', 'gif', 'bmp')):
    image_paths = []

    # List all files in the folder
    files = os.listdir(folder_path)

    for file in files:
        # Check if the file has a valid image extension
        if any(file.lower().endswith(ext) for ext in extensions):
            # Construct the full path to the image
            image_path = os.path.join(folder_path, file)
            image_paths.append(image_path)

    return image_paths

# Example usage
folder_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files"
image_paths = get_image_paths(folder_path)
# print(os.listdir(folder_path))
# Print the paths or use them as needed
img_list = []
print(image_paths)
