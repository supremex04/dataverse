import os

def get_image_paths(folder_path, extensions=('jpg', 'jpeg', 'png', 'gif', 'bmp')):
    image_paths = []

    files = os.listdir(folder_path)

    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            image_path = os.path.join(folder_path, file)
            image_paths.append(image_path)

    return image_paths

folder_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files"
image_paths = get_image_paths(folder_path)
# print(os.listdir(folder_path))
img_list = []
print(image_paths)
