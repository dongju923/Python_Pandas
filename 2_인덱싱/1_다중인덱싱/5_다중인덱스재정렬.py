import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(6, 3), index=[['a', 'a', 'b', 'b', 'c', 'c'], [
                  1, 2, 1, 2, 1, 2]], columns=['c1', 'c2', 'c3'])
print(df)

df.sort_index()
print(df['a':'b'])
print(df.unstack(level=0))
print(df.unstack(level=1))
print(df.stack())
print(df.reset_index(level=0))
print(df.reset_index(level=(0, 1)))
print(df.set_index(['c1']))
