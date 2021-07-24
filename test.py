import random
import pandas as pd


df = pd.read_csv('wordlist.csv', index_col=0)
print(random.choice(df.loc['food_firsthalf']))

