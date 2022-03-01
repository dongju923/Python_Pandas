import numpy as np
import pandas as pd


s = pd.Series([1., 2., -999., 3., -1000., 4.])
print(s)
print(s.replace(-999, np.nan))
print(s.replace([-999, -1000], np.nan))
print(s.replace([-999, -1000], 0))
