import numpy as np
import pandas as pd

index = [("a", "En"), ("a", "Ma"), ("b", "En"), ("b", "Ma"),
         ("c", "En"), ("c", "Ma"), ("d", "En"), ("d", "Ma")]
value = [10, 20, 30, 40, 50, 60, 70, 80]

score = pd.Series(value, index=index)
print(score)

index = pd.MultiIndex.from_tuples(index)
print(index)
score = score.reindex(index)
print(score)

# Series 객체에서는 정렬을 하지 않으면 슬라이싱 불가
score = score.sort_index()
print(score[:, "En"])
print(score['a':"c"])
