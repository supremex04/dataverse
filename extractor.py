import base64
import requests
import image_collection
from txt_writer import encode_image
from txt_writer import addtotxt
import os

api_key = ""

folder_path = "C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files"
names = os.listdir(folder_path)
count = 0
image_path = ['C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\0869be20-07ec-40c9-be93-fe9d6b0ae5dd.jpeg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\0b6fcb50-b157-4457-b3a3-06779f91b8b8.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\151d0d84-bfb4-4338-8839-90d69a1a3074.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\19d98817-caf1-4e5a-b8b2-22881ecef5d4.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\21dd0238-661b-4d4a-8d6f-8b7717d229fc.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\281dec77-e364-494e-9a67-0d862b5a509e.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\292518c6-bfd4-4096-92a1-7df63faf0860.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\2a8677b9-b29e-4c93-86e5-56d4c38cb7fc.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\2ec7883e-dafe-4cc3-9836-7314ace98c14.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\3e2ef304-3cb7-4452-87b8-102bea1c2908.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\4907a532-bf75-4bc4-a08c-06f9d3f00306.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\4cfc9619-5dd4-4307-90b6-04d20ba6db3b.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\4d972974-e804-4c67-af7c-071b16d1d35a.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\522a7c5f-166c-479f-8801-10d43d83a3b9.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\608cb44c-46b7-405e-acfa-1bb8ed4e9cf8.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\69b77ea7-6f8a-4eba-9568-8c33136879c3.jpeg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\6a620b62-167a-466e-961d-63cac09ba563.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\6fab0ac5-e856-43af-a2ed-621d1a15818a.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\70de9d18-4aff-40bc-b60a-db7dec2b5af7.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\72c641c1-d057-48ab-9d1f-2abb143c691d.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\77502028-18e6-4a51-9b7d-0cc5f4a68726.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\77ed1272-512c-4389-8a38-3798084cb073.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\7b450c61-a83d-4843-8404-0828b0d62891.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\8e00367b-25b3-401b-bf8e-e1cfc801e4ae.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\9b650c90-ad5c-4f07-b04a-b58e33318398.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\9d396ae4-7abe-4aa5-8481-11df722e49c7.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\a7e533f9-fea3-453e-b135-6b6d9d3c63a6.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\aacc330f-a0ad-4248-bce9-9eab83818e2b.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\b06572e1-a3c6-43a8-8e33-a2d8b5669da3.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\b33b5ce3-4ff8-4c88-aa43-137875bcb754.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\c4141ea0-72cc-46f8-826f-a5d80451f8e5.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\cdfb3904-b918-4b56-ab73-20d3ffcccca5.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\e2befb75-c0e9-4c7f-befd-3fc16e4b9acb.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\e32e1986-37d9-46c9-9e63-551a3e6ee83a.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\e34b2104-7996-488f-a71a-af1819bd8f9f.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\e45e92a6-3cd7-495a-8e47-ab95d1cdda3e.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\e8d8c551-7a88-4f7d-bccf-4b205317b21e.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\ee3a5b7c-ed1b-4a89-9f36-ee403616cf5d.jpg', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\f0cb78a6-b501-4962-8baa-e5d8180d625a.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\f50b68b8-543f-48ef-999d-b1b142c1baeb.png', 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\test-20240120T143754Z-001\\test\\files\\fd28f5e7-fc19-4f23-8dec-9a87b40f1a15.jpg']

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}
for path in image_path:
  base64_image  = encode_image(path)
  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "This is a representation of invoice. I need three things, titles and product detail and technical detail (all in short cut).Both should be to the point without explanations. The output should be in key: value pair of Titles:, Product Details: and Technical Details: . All key and values within '' and the three main keys separated by comma and no curly brackets anywhere. The invoice has a main section, generally at the middle, in a table. If there is a table, it has several columns and columns have title. If it doesnt have a table, its well fromatted into columns and columns have title. Give me the title of those columns. And the product detail, quantity and any other techical detail mentioned generally in the table."          },
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
  resp = response.json()
  print(resp['choices'][0]['message']['content'])
  addtotxt(names[count], resp['choices'][0]['message']['content'])
  count +=1