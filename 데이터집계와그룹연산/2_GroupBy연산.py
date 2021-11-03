import pandas as pd
import numpy as np


df = pd.DataFrame({"c1": ['a', 'b', 'b', 'c', 'd', 'b', 'd'], "c2": [
                  'A', 'B', 'B', 'A', 'D', 'C', 'C'], "c3": np.random.randint(7), "c4": np.random.random(7)})
print(df)

print(df.dtypes)

print(df["c3"].groupby(df['c1']).mean())
print(df['c4'].groupby(df['c2']).std())
print(df['c4'].groupby([df['c1'], df['c2']]).mean())
print(df['c4'].groupby([df['c1'], df['c2']]).mean().unstack())
print(df.groupby('c1').mean())
print(df.groupby(['c1', 'c2']).mean())

for c1, group in df.groupby('c1'):
    print(c1)
    print(group)
# for문을 이용한 c1을 기준으로 group들을 반환

print(df.groupby(['c1', 'c2'])['c4'].mean())
print(df.groupby(['c1', 'c2'], as_index=False)['c4'].mean())
print(df.groupby(['c1', 'c2'], group_keys=False)['c4'].mean())


def top(dataframe, n, column):
    return df.sort_values(by=column)[-n:]


print(top(df, 5, 'c2'))
