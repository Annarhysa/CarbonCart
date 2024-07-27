import easyocr

image = '../data/images/digital_list.jpg'

def image_list(image):

    # Initialize the easyocr Reader
    reader = easyocr.Reader(['en'])

    # Path to the image file
    image_path = image

    # Use easyocr to extract text
    result = reader.readtext(image_path)

    # Extracted text
    extracted_text = '\n'.join([res[1] for res in result])

    return extracted_text
    # # Print the extracted text
    # print(extracted_text)

    # # Save the extracted text to a file
    # with open('../data/extracted_text/extracted.txt', 'w') as file:
    #     file.write(extracted_text)

    # print(f"Extracted text has been saved to 'extracted_text.txt'")

# image_list(image)
