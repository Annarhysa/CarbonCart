from paddleocr import PaddleOCR

image = '../data/images/digital_list.jpg'

def image_list(image_path):
    # Initialize the PaddleOCR Reader
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # use_angle_cls=True helps in detecting the text orientation

    # Use PaddleOCR to extract text
    result = ocr.ocr(image_path, cls=True)

    # Extracted text
    extracted_text = ""
    for line in result:
        for word_info in line:
            extracted_text += word_info[1][0] + ' '
        extracted_text += '\n'

    return extracted_text.strip()

# Example usage
extracted_text = image_list(image)
print(extracted_text)
