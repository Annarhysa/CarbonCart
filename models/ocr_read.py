from paddleocr import PaddleOCR


def image_list(image_path):
    # Initialize the PaddleOCR Reader
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # use_angle_cls=True helps in detecting the text orientation

    # Use PaddleOCR to extract text
    result = ocr.ocr(image_path, cls=True)

    # Extracted text
    extracted_text = []
    for line in result:
        for word_info in line:
            extracted_text.append(word_info[1][0])

    return extracted_text
