import numpy as np
import pandas as pd

p = pd.Period(2020, freq='A-JAN')
print(p)
print(p+2)
print(p-3)

p1 = pd.Period(2010, freq='A-JAN')
p2 = pd.Period(2020, freq='A-JAN')
print(p2-p1)

pr = pd.period_range('2020-01-01', periods=6, freq='M')
print(pd.Series(np.random.randn(6), index=pr))

p = pd.Period('2020', freq='A-FEB')
print(p.asfreq('M', how='start'))
print(p.asfreq('M', how='end'))
