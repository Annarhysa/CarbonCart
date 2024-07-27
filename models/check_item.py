import pandas as pd
import numpy as np

data = pd.read_csv('data/items_cp_stats.csv')

with open('data/extracted_text.txt','r') as f:
    myList = f.readlines()
    myList = map(lambda x: x.replace('\n',''),myList)

