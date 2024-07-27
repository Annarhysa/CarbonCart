from flask import Flask, request, render_template, redirect, url_for, session
import os
import pandas as pd
from models.ocr_read import image_list

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'your_secret_key'  # Needed for session management

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load dataset
df = pd.read_csv('./data/items_cp_stats.csv')

def extract_item_quantity(line):
    words = line.split()
    quantity = None
    for i, word in enumerate(words):
        if word.lower().endswith('kg'):
            try:
                quantity = float(word.lower().replace('kg', ''))
            except ValueError:
                continue
            item = ' '.join(words[:i])
            return item, quantity
    return line, quantity

def process_user_input(inputs, data):
    items = data['FOOD COMMODITY ITEM'].str.lower().unique()
    commodity_typologies = data['FOOD COMMODITY TYPOLOGY'].str.lower().unique()
    result = {}
    dropdown_data = {}
    item_details = {}

    for line in inputs:
        item, quantity = extract_item_quantity(line)
        item = item.lower()
        if item in items:
            result[item] = quantity
        else:
            matched_typology = [typology for typology in commodity_typologies if typology in item]
            if matched_typology:
                specific_items = data[data['FOOD COMMODITY TYPOLOGY'].str.lower() == matched_typology[0]]['FOOD COMMODITY ITEM']
                dropdown_data[item] = specific_items.tolist()
                result[item] = None
            else:
                item_details[item] = quantity

    session['dropdown_data'] = dropdown_data
    session['item_details'] = item_details
    return result

def carbon_emission(inputs, data):
    result = {}
    items = data['FOOD COMMODITY ITEM'].str.lower().unique()
    
    for item, quantity in inputs.items():
        item = item.lower()
        quantity = float(quantity)  # Ensure quantity is a number
        
        if item in items:
            # Get the median carbon emission for the item
            median_emission = data.loc[data['FOOD COMMODITY ITEM'].str.lower() == item, 'median'].values[0]
            # Calculate the total emission
            total_emission = round(quantity * median_emission, 2)
            result[item] = total_emission
        else:
            result[item] = 'Item not found in dataset'

    return result

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
        text = image_list(image_path)
        result_dict = process_user_input(text, df)
        return render_template('processed.html', text=result_dict)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form
    processed_data = {}
    dropdown_data = session.get('dropdown_data', {})
    
    for key, value in form_data.items():
        if key.startswith('item_'):
            item_key = key.split('_', 1)[1]
            quantity = form_data.get(f'quantity_{item_key}', None)
            
            # Check if the item_key is in dropdown_data
            if item_key in dropdown_data:
                # Use the user's selection from the dropdown
                selected_item = form_data.get(key)
                if selected_item:
                    processed_data[selected_item.lower()] = quantity
            else:
                processed_data[item_key.lower()] = quantity
    
    # Now, processed_data has the correct item names and quantities
    result = carbon_emission(processed_data, df)
    
    return render_template('result.html', data=result)


if __name__ == '__main__':
    app.run(debug=True)
