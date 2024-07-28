import pandas as pd

def recommend_alternatives(processed_data, data):
    recommendations = {}
    
    for item, quantity in processed_data.items():
        # Ensure quantity is a number
        if quantity is None:
            continue
        quantity = float(quantity)

        # Find the current item details
        item_data = data[data['FOOD COMMODITY ITEM'].str.lower() == item.lower()]
        if item_data.empty:
            continue

        current_emission = item_data['median'].values[0]
        typology = item_data['FOOD COMMODITY TYPOLOGY'].values[0]

        # Filter for items in the same typology with lower emissions
        alternatives = data[(data['FOOD COMMODITY TYPOLOGY'] == typology) & 
                            (data['median'] < current_emission)]

        if not alternatives.empty:
            # Sort by emission values and recommend the top items
            recommended_items = alternatives.sort_values(by='median').head(5)
            recommendations[item] = recommended_items['FOOD COMMODITY ITEM'].tolist()

    return recommendations
