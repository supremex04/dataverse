import csv
import os
from image_collection import get_image_paths
folder_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\train-20240120T143828Z-001\\train\\files"
image_paths = os.listdir(folder_path)
print(image_paths)
# Specify the path for the existing CSV file
existing_csv_file_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\4keys.csv"

# Specify the path for the new CSV file
new_csv_file_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\4keyswithname.csv"

# Specify the new header name and item value
new_header_name = "Image name"
new_item_value = "New Item Value"

# Read existing data from CSV file
existing_data = []
with open(existing_csv_file_path, 'r', newline='', encoding='utf-8') as existing_csv_file:
    csv_reader = csv.reader(existing_csv_file)
    existing_data = list(csv_reader)

# Add new header to the header row
existing_data[0].append(new_header_name)
count =0
# Add the new item to each row
for row in existing_data[1:]:
    new_item_value = image_paths[count]
    row.append(new_item_value)
    count +=1

# Write modified data to the new CSV file
with open(new_csv_file_path, 'w', newline='', encoding='utf-8') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)
    csv_writer.writerows(existing_data)

print(f"Data has been written to: {new_csv_file_path}")
