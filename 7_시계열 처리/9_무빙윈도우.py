import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(300, 4), index=pd.date_range(
    '2020-01-01', periods=300, freq='D'), columns=(['c1', 'c2', 'c3', 'c4']))
print(df)
print(df.rolling(30).mean())
print(df.rolling(30).mean().plot())
print(df.rolling(60).mean())
print(df.c1.rolling(30).mean())
print(df.c2.rolling(30, min_periods=10).std())
print(df.c2.rolling(60, min_periods=10).std()[10:50])
print(df.c2.rolling('20D', min_periods=10).std()[10:50])
