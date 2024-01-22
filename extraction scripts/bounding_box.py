import easyocr
import cv2

reader = easyocr.Reader(['en'], gpu=True)
img_path = '/home/samriddhi/Documents/DV_trainimg/9c8af380-546d-46dd-b78e-af791f27ab2f.png'
img = cv2.imread(img_path)

results = reader.readtext(img, detail=1, paragraph=False)

keywords_to_filter = ["Total","Date","No.","Invoice Total", "Invoice Date", "Due Date", "Invoice #"]

keyword_bboxes = {}

for i, (bbox, text, prob) in enumerate(results):
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()

    # Check if the recognized text is in the list of keywords
    if any(keyword.lower() in text.lower() for keyword in keywords_to_filter):
        # Extract the value to the right or below
        if i + 1 < len(results):
            value_bbox, _, _ = results[i + 1]

            keyword_bboxes[text] = value_bbox

for bbox in keyword_bboxes.values():
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    cv2.rectangle(img, tl, br, (0, 255, 0), 2)


cv2.imshow("Image", img)
cv2.waitKey(0)

print("Keyword and Bounding Box Coordinates:")
for keyword, bbox in keyword_bboxes.items():
    print(f"{keyword}: {bbox}")