import numpy as np
import pandas as pd

# 인덱스 연산자

### append(other) ###
# 인덱스 객체를 추가한 새로운 인덱스 반환

### difference(other, sort=None) ###
# 인덱스의 차집합 반환

### intersection(other, sort=False), & ###
# 인덱스의 교집합 반환

### union(other, sort=None), | ###
# 인덱스의 합집합 반환, 중복 X

### isin(values, level=None) ###
# 인덱스가 존재하는지 여부를 불리언 배열로 변환

### delete(loc) ###
# 인덱스가 삭제된 새로운 인덱스 반환

### drop(labels, errors='raise') ###
# 값이 삭제된 새로운 인덱스 반환

### insert(loc, item) ###
# 인덱스가 추가된 새로운 인덱스 반환

### is_monotonic() ###
# 인덱스가 단조성을 가지면 True

### is_unique() ###
# 중복되는 인덱스가 없다면 True

### unique() ###
# 인덱스에서 중복되는 요소를 제거하고 유일한 값만 반환


idx1 = pd.Index([1, 2, 4, 6, 8])
idx2 = pd.Index([2, 4, 5, 6, 7])
print(idx1)
print(idx2)

print(idx1.append(idx2))
# Int64Index([1, 2, 4, 6, 8, 2, 4, 5, 6, 7], dtype='int64')
print(idx1.difference(idx2))
# Int64Index([1, 8], dtype='int64')
print(idx1.intersection(idx2))
# Int64Index([2, 4, 6], dtype='int64')
print(idx1.union(idx2))
# Int64Index([1, 2, 4, 5, 6, 7, 8], dtype='int64')
print(idx1.isin(idx2))
# [False  True  True  True False]
print(idx2.isin(idx1))
# [ True  True False  True False]
print(idx1.delete(0))
# Int64Index([2, 4, 6, 8], dtype='int64')
print(idx1.drop(2))
# Int64Index([1, 4, 6, 8], dtype='int64')
print(idx1.insert(5, 20))
# Int64Index([1, 2, 4, 6, 8, 20], dtype='int64')
print(idx1.is_monotonic)
# True
print(idx1.is_unique)
# True
