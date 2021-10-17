import numpy as np
import pandas as pd

### add(other, axis='columns', level=None, fill_value=None) ###
a = np.random.randint(1, 10, (3, 3))
print(a)
print(a[0])
print(a+a[0])

df = pd.DataFrame(a, columns=list('ABC'))
print(df)
print(df.iloc[0])
print(df+df.iloc[0])

print(df.add(df.iloc[0], axis=1))
# axis=1: index

df = pd.DataFrame(a, columns=[0, 1, 2])
print(df.add(df.iloc[0], axis=0))
# axis=0: columns
