from openai import OpenAI

import base64
import requests

api_key = ""
image_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\train-20240120T143828Z-001\\train\\files\\5f5f7af4-933d-47f6-9fe0-ab05eab6ef71.jpg"

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

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
                "text": "This is a representation of invoice. It has Invoice Number(bill number or receipt number), Invoice Date(Billing date) and the main table which has most of the information about purchase. Provide me the bounding box of these three things in the format of Invoice Number: Invoice Date: Total bbox: and Table bbox:"},
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