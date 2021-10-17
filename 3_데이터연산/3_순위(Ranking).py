import numpy as np
import pandas as pd

s = pd.Series([-2, 4, 7, 3, 5, 0, -4, 2, 6, 7])

print(s.rank())
print(s.rank(method='first'))
# 중복 없이 먼저 온 값이 높은 순위로 지정
print(s.rank(method='max'))
# 같은 값을 가지는 그룹을 높은 순위로 지정
print(s.rank(method='min'))
# 같은 값을 가지는 그룹을 낮은 순위로 지정
print(s.rank(method='average'))
# 기본값, 순위에 같은 값을 가지는 항목들의 평균값을 사용
print(s.rank(method='dense'))
# 같은 그룹 내에서 모두 같은 순위를 적용하지 않고 1씩 증가
