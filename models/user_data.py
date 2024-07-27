import pandas as pd

# Read user input from a text file
def read_user_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


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

    for line in inputs:
        item, quantity = extract_item_quantity(line)
        item = item.lower()

        # Check if the item exists in the dataset
        if item in items:
            if quantity is None:
                quantity = input(f"Enter the quantity in KG for {item}: ").strip()
            result[item] = quantity
        else:
            # Check if it's a general category like 'beer'
            matched_typology = [typology for typology in commodity_typologies if typology in item]
            if matched_typology:
                specific_items = data[data['FOOD COMMODITY TYPOLOGY'].str.lower() == matched_typology[0]]['FOOD COMMODITY ITEM']
                specific_item = input(f"Please specify the type for {item}: {list(specific_items)}: ").strip()
                if specific_item.lower() in items:
                    if quantity is None:
                        quantity = input(f"Enter the quantity in KG for {specific_item}: ").strip()
                    result[specific_item] = quantity
                else:
                    print(f"Specific item '{specific_item}' not found in the dataset.")
            else:
                print(f"Item '{item}' not found in the dataset.")

    return result
