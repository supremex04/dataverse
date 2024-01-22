import csv
import os
from image_collection import get_image_paths
folder_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files"
image_paths = os.listdir(folder_path)
print(image_paths)
existing_csv_file_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\extractions\\testtablekeys.csv"

new_csv_file_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\extractions\\testtablekeyswithname.csv"

new_header_name = "Image name"
new_item_value = ""

existing_data = []
with open(existing_csv_file_path, 'r', newline='', encoding='utf-8') as existing_csv_file:
    csv_reader = csv.reader(existing_csv_file)
    existing_data = list(csv_reader)

existing_data[0].append(new_header_name)
count =0
for row in existing_data[1:]:
    new_item_value = image_paths[count]
    row.append(new_item_value)
    count +=1

with open(new_csv_file_path, 'w', newline='', encoding='utf-8') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)
    csv_writer.writerows(existing_data)

print(f"Data has been written to: {new_csv_file_path}")
