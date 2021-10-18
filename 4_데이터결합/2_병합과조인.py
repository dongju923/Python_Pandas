import numpy as np
import pandas as pd

### merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None) ###

df1 = pd.DataFrame({"학생": ["김씨", "이씨", "박씨", "한씨"],
                   "학과": ["경영", "컴퓨터", "통계", "교육"]})
print(df1)

df2 = pd.DataFrame({"학생": ["김씨", "이씨", "박씨", "한씨"],
                   "입학년도": [2012, 2016, 2020, 2019]})
print(df2)

df3 = pd.merge(df1, df2)
print(df3)

df4 = pd.DataFrame({"학과": ["경영", "컴퓨터", "통계", "교육"],
                   "학과장": ["황씨", "장씨", "안씨", "정씨"]})
print(df4)

print(pd.merge(df3, df4))

df5 = pd.DataFrame({"학과": ["경영", "컴퓨터", "컴퓨터", "통계", "교육", "교육"], "과목": [
                   "경영개론", "기초수학", "물리학", "프로그래밍", "운영체제", "확률론"]})
print(df5)

print(pd.merge(df1, df5))
print(pd.merge(df1, df5, on='학과'))
# 학과 기준으로 병합

df6 = pd.DataFrame({"이름": ["김씨", "이씨", "박씨", "한씨"], "성적": [90, 80, 50, 60]})
print(df6)

print(pd.merge(df1, df6, left_on="학생", right_on="이름"))
# 칼럼명이 다르고 데이터는 같을때 left_on, right_on 키워드를 사용하여 같이 반환
print(pd.merge(df1, df6, left_on="학생", right_on="이름").drop("이름", axis=1))
# 칼럼명이 다르지만 데이터가 같아서 자르고 싶을때 drop함수를 이용함

df7 = pd.DataFrame({"이름": ["홍길동", "이순신", "임꺽정"], "주문음식": ["햄버거", "피자", "짜장면"]})
print(df7)
df8 = pd.DataFrame({"이름": ["홍길동", "이순신", "김유신"], "주문음료": ["콜라", "사이다", "커피"]})
print(df8)

print(pd.merge(df7, df8))
# 칼럼과 값이 매치되는 것만 반환
print(pd.merge(df7, df8, how="outer"))
# 칼럼과 값이 매치가 안되는것도 NaN값으로 반환
print(pd.merge(df7, df8, how="left"))
# df7에 있는 값만 기준으로 반환
print(pd.merge(df7, df8, how="right"))
# df8에 있는 값만 기준으로 반환

df9 = pd.DataFrame({"이름": ["김씨", "이씨", "박씨", "한씨"], "순위": [3, 2, 4, 1]})
print(df9)
df10 = pd.DataFrame({"이름": ["김씨", "이씨", "박씨", "한씨"], "순위": [4, 1, 3, 2]})
print(df10)

print(pd.merge(df9, df10, on="이름"))
print(pd.merge(df9, df10, on="이름", suffixes=["_인기", "_성적"]))
