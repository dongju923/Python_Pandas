import numpy as np
import pandas as pd

# 복잡한 연산도 순식간에 수행 가능
nrows, nclos = 100000, 100
df1, df2, df3, df4 = (pd.DataFrame(np.random.rand(nrows, nclos))
                      for _ in range(4))
print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())
# 일부분만 잘라서 출력

print(df1+df2+df3+df4)
print(pd.eval('df1+df2+df3+df4'))
print(df1*df2 / (-df3*df4))
