import numpy as np
import pandas as pd

a = np.random.randint(1, 10, (3, 3))
print(a)

print(a ** a[0])

df = pd.DataFrame(a, columns=list("ABC"))
print(df)

### pow(other, axis='columns', level=None, fill_value=None) ###
print(df.pow(df.iloc[0]))
print(df ** 2)
