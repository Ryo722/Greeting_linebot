import random
import pandas as pd


df = pd.read_csv('wordlist.csv', index_col=0)
print(chr(int(random.choice(df.loc['emoji']))))
print("\U0001F605")
