import numpy as np
import pandas as pd


df = pd.DataFrame({'c1': ['a', 'b', 'c']*2 + ['b'] + ['c'],
                   'c2': [1, 2, 1, 1, 2, 3, 3, 4]})
print(df)
print(df.duplicated())
print(df.drop_duplicates())
