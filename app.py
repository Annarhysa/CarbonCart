import base64
from io import BytesIO
from flask import Flask, render_template, request, redirect
from markupsafe import escape
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/test', methods=['GET', 'POST'])
def test():
    image_data = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file:
            image = Image.open(file)
            buffered = BytesIO()
            image.save(buffered, format='JPEG')
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
            image_data = f"data:image/jpeg;base64,{img_str}"

    return render_template('test.html', image_data=image_data)

@app.route('/hello/<name>')
def hello(name):
    return f"Hello {escape(name)}"


if __name__ == '__main__':
    app.run(debug=True)
