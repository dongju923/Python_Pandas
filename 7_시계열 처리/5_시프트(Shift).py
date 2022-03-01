import pandas as pd
import numpy as np

ts = pd.Series(np.random.random(5), index=pd.date_range(
    '2022-01-11', periods=5, freq='B'))
print(ts)

print(ts.shift(1))
print(ts.shift(-2))
print(ts.shift(2, freq='B'))
# 인덱스가 시프트 됨
