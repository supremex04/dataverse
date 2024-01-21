import cv2
import easyocr
import cvlib as cv
from cvlib.object_detection import draw_bbox
# image_path = "/home/samriddhi/Documents/DV_trainimg/0d3e37dd-23db-4d97-b3e4-50486901c527.jpg"

def extract_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    return result

def detect_objects(image_path):
    image = cv2.imread(image_path)
    bbox, label, conf = cv.detect_common_objects(image)
    return bbox, label

def find_entity_bbox(results, entity):
    for (bbox, text) in results:
        if entity.lower() in text.lower():
            return bbox
    return None

def main(image_path):
    # Extract text using OCR
    ocr_results = extract_text(image_path)

    # Detect objects using object detection
    object_bbox, object_labels = detect_objects(image_path)

    # Find bounding box for specific entities
    invoice_number_bbox = find_entity_bbox(ocr_results, "invoice number")
    issue_date_bbox = find_entity_bbox(ocr_results, "issue date")
    total_amount_bbox = find_entity_bbox(ocr_results, "total amount")
    table_bbox = find_entity_bbox(ocr_results, "table")

    # Draw bounding boxes on the image
    image = cv2.imread(image_path)
    draw_bbox(image, object_bbox, object_labels)
    if invoice_number_bbox:
        cv2.rectangle(image, (invoice_number_bbox[0][0], invoice_number_bbox[0][1]),
                      (invoice_number_bbox[2][0], invoice_number_bbox[2][1]), (0, 255, 0), 2)
    if issue_date_bbox:
        cv2.rectangle(image, (issue_date_bbox[0][0], issue_date_bbox[0][1]),
                      (issue_date_bbox[2][0], issue_date_bbox[2][1]), (0, 255, 0), 2)
    if total_amount_bbox:
        cv2.rectangle(image, (total_amount_bbox[0][0], total_amount_bbox[0][1]),
                      (total_amount_bbox[2][0], total_amount_bbox[2][1]), (0, 255, 0), 2)
    if table_bbox:
        cv2.rectangle(image, (table_bbox[0][0], table_bbox[0][1]),
                      (table_bbox[2][0], table_bbox[2][1]), (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Bounding Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'C:\\Users\\bhand\\Desktop\\OpenCV\\dataverse\\train-20240120T143828Z-001\\train\\files\\00524b56-4fe9-4fa4-b154-23394b827c86.png'  # Replace with the path to your image
    main(image_path)