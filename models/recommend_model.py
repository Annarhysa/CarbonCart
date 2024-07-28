import pandas as pd

def recommend_alternatives(processed_data, data):
    df = pd.read_csv('data/items_cp_stats.csv')
    recommendations = {}
    for item, quantity in processed_data.items():
        # Ensure quantity is a number
        if quantity is None:
            continue
        quantity = float(quantity)

        # Get the median emission for the current item
        current_emission = data.loc[data['FOOD COMMODITY ITEM'].str.lower() == item, 'median'].values[0]
        total_current_emission = quantity * current_emission

        # Find alternatives in the same typology or group with lower emissions
        typology = data.loc[data['FOOD COMMODITY ITEM'].str.lower() == item, 'FOOD COMMODITY TYPOLOGY'].values[0]
        group = data.loc[data['FOOD COMMODITY ITEM'].str.lower() == item, 'FOOD COMMODITY GROUP'].values[0]

        # Filter for items in the same typology or group
        alternatives = data[
            (data['FOOD COMMODITY TYPOLOGY'] == typology) |
            (data['FOOD COMMODITY GROUP'] == group)
        ]

        # Filter for items with lower emissions than the current item
        lower_emission_alternatives = alternatives[alternatives['median'] < current_emission]

        if not lower_emission_alternatives.empty:
            # Sort by emission values and recommend the top items
            recommended_items = lower_emission_alternatives.sort_values(by='median').head(5)
            recommendations[item] = recommended_items['FOOD COMMODITY ITEM'].tolist()

    return recommendations