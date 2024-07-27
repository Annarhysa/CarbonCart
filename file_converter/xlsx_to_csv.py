import pandas as pd

# Path to the XLSX file
xlsx_file = '../data/food_data.xlsx'

# Name of the sheet you want to convert
sheet_name = 'SEL CF  ITEMS STAT'

# Read the XLSX file into a pandas DataFrame
df = pd.read_excel(xlsx_file, sheet_name=sheet_name)

# Path to save the CSV file
csv_file = '../data/items_cp_stats.csv'

# Convert the DataFrame to CSV
df.to_csv(csv_file, index=False)