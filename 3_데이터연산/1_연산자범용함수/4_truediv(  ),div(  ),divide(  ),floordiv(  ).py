import numpy as np
import pandas as pd

a = np.random.randint(1, 10, (3, 3))
print(a)

print(a/a[1])

df = pd.DataFrame(a, columns=list("ABC"))
print(df)

print(df/df.iloc[0])
print(df.div(df.iloc[1]))
print(df.divide(df.iloc[1]))

### truediv(ther, axis='columns', level=None, fill_value=None) ###
print(df.truediv(df.iloc[0]))

### floordiv(other, axis='columns', level=None, fill_value=None) ###
print(df//df.iloc[0])
print(df.floordiv(df.iloc[0]))
