import numpy as np
import pandas as pd

s = pd.Series([0, 1, 2, 3, 4], index=['a', 'b', 'c', 'd', 'e'])
print(s)

print(s['b'])
# 1
print(s[1])
# 1
print('b' in s)
# True
print(4 in s)
# False
print(s.keys())
# Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print(s.index)
#Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print(s.values)
# [0 1 2 3 4]
print(s.items())
# <zip object at 0x0000020297AE5348>
print(list(s.items()))
# [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]
s['f'] = 5
# f라는 인덱스와 5라는 값 추가
print(s)
print(s['a':'d'])
print(s[0:4])
print(s[(s > 1) & (s < 4)])
print(s[['a', 'c', 'f']])
