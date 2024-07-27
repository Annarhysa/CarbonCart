from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import easyocr
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)
        # Perform OCR on the image
        text = perform_ocr(image_path)
        return render_template('result.html', text=text)

def perform_ocr(image_path):
    result = reader.readtext(image_path)
    print(result)
    extracted_text = []
    for _, text, _ in result:
        extracted_text.append(text)
    # extracted_text = ' '.join([text for _, text, _ in result])
    return extracted_text

if __name__ == '__main__':
    app.run(debug=True)
