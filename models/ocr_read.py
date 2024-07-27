import easyocr

# Initialize the easyocr Reader
reader = easyocr.Reader(['en'])

# Path to the image file
image_path = '../data/images/digital_list.jpg'

# Use easyocr to extract text
result = reader.readtext(image_path)

# Extracted text
extracted_text = '\n'.join([res[1] for res in result])

# Print the extracted text
print(extracted_text)

# Save the extracted text to a file
with open('../data/extracted_text.txt', 'w') as file:
    file.write(extracted_text)

print(f"Extracted text has been saved to 'extracted_text.txt'")
