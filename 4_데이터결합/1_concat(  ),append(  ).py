import numpy as np
import pandas as pd

### concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True) ###
s1 = pd.Series(['a', 'b'], index=[1, 2])
s2 = pd.Series(['c', 'd'], index=[3, 4])

print(pd.concat([s1, s2]))


# DataFrame을 생성하는 함수
def create_df(idx, cols):
    data = {c: [str(c.lower()) + str(i) for i in idx]for c in cols}
    return pd.DataFrame(data, idx)


df1 = create_df([1, 2], "AB")
df2 = create_df([3, 4], "AB")
print(pd.concat([df1, df2]))

df3 = create_df([0, 1], "AB")
df4 = create_df([0, 1], "CD")
print(pd.concat([df3, df4]))

print(pd.concat([df1, df3]))
# print(pd.concat([df1, df3]), verify_integrity=True)
print(pd.concat([df1, df3], ignore_index=True))
# 겹치는 인덱스를 무시하고 반환
print(pd.concat([df1, df2], keys=['X', 'Y']))
# 멀티인덱스처럼 인덱스에 key를 추가
print(pd.concat([df3, df4], axis=1))

df5 = create_df([1, 2], "ABC")
df6 = create_df([3, 4], "BCD")
print(pd.concat([df5, df6]))

print(pd.concat([df5, df6], join='inner'))
# 둘다 존재하는 데이터만 반환

### append(other, ignore_index=False, verify_integrity=False, sort=Falses) ###
print(df5.append(df6))
