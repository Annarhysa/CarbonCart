import pandas as pd

from spellchecker import SpellChecker

data = pd.read_csv('../data/items_cp_stats.csv')

food = data['FOOD COMMODITY TYPOLOGY'].unique()
new = []

for i in food:
    new.append(i)

with open('../data/extracted_text/food_items.txt', 'w') as file:
    # Write each item on a new line
    for item in new:
        file.write(f"{item}\n")


spell = SpellChecker()

def suggest_similar_words(text):
    suggestions = {}
    words = text.split()
    for word in words:
        # Check if the word is misspelled
        if word not in spell:
            # Get a list of suggested words
            suggested_words = spell.candidates(word)
            suggestions[word] = list(suggested_words)
    return suggestions

suggestions = []
for i in new:
    suggestions.append(suggest_similar_words(i))

with open('../data/extracted_text/typos.txt', 'w') as file:
    file.write(f"{suggestions}\n")
