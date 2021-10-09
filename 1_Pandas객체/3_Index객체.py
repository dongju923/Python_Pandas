import pandas as pd
import numpy as np

### Index ###
# 일반적인 Index 객체이며, Numpy 배열 형식으로 축의 이름 표현

### Int64Index ###
# 정수 값을 위한  Index

### MultiIndex ###
# 단일 축에 여러 단계 색인을 표현하는 계층적 Index객체(튜플의 배열과 유사)
# .from_arrays
# .from_product
# .from_tuples
# .from_frame

### DatatimeIndex ###
# Numpy의 datetime64 타입으로 타임스탬프 저장

### PeriodIndex ###
# 기간 데이터를 위한 Index

idx = pd.Index([2, 4, 6, 8, 10])
print(idx)
print(idx[1])
print(idx[1:2:2])
print(idx[-1::])
print(idx[::2])

# 정보확인
print(idx.size)
print(idx.shape)
print(idx.ndim)
print(idx.dtype)

ex_arr = np.array([['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
                  ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']])
print(ex_arr)
print(pd.MultiIndex.from_arrays(ex_arr, names=["one", "two"]))
