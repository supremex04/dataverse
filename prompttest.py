from openai import OpenAI

import base64
import requests

api_key = "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"
image_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\train-20240120T143828Z-001\\train\\files\\56415ebf-98cc-4050-a4eb-58de6c5d22bf.jpg"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                # "text": "What is in this image?"
                "text": "This is a representation of invoice. I need three things, titles and product detail and technical detail (all in short cut).Both should be to the point without explanations. The output should be in key: value pair of Titles:, Product Details: and Technical Details: . All key and values within '' and the three main keys separated by comma. The invoice has a main section, generally at the middle, in a table. If there is a table, it has several columns and columns have title. If it doesnt have a table, its well fromatted into columns and columns have title. Give me the title of those columns. And the product detail, quantity and any other techical detail mentioned generally in the table."            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    }
],
"max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(type(response))
resp = response.json()
print(resp['choices'][0]['message']['content'])