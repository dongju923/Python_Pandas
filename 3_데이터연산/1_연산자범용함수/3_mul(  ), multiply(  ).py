import numpy as np
from numpy.lib.index_tricks import AxisConcatenator
import pandas as pd

a = np.random.randint(1, 10, (3, 3))
print(a)
print(a*a[0, 0])

df = pd.DataFrame(a, columns=list("ABC"))
print(df)
print(df*df.iloc[1, 0])

print(df.mul(df.iloc[1]))
print(df.multiply(df.iloc[2], axis=1))
