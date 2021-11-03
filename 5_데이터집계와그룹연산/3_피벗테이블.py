"""피벗테이블 함수
values: 집계하려는 칼럼이름 혹은 이름의 리스트. 기본적으로 모든 숫자 컬럼 집계
index: 피벗테이블의 인덱스를 그룹으로 묶을 컬럼 이름이나 그룹 키
columns: 피벗테이블의 컬럼을 그룹으로 묶을 컬럼 이름이나 그룹 키
aggfunc: 집계 함수나 함수 리스트. 기본값으로 mean()이 사용
fill_value: 결과 테이블에서 누락된 값 대체를 위한 값
dropna: True인 경우 모든 항목이 NA인 컬럼은 포함하지 않음
margins: 부분합이나 총계를 담기 위한 인덱스/컬럼 추가 여부. Defalt=False
"""
import pandas as pd
import numpy as np


df = pd.DataFrame({"c1": ['a', 'b', 'b', 'c', 'd', 'b', 'd'], "c2": [
                  'A', 'B', 'B', 'A', 'D', 'C', 'C'], "c3": np.random.randint(7), "c4": np.random.random(7)})
print(df)

print(df.pivot_table(['c3'], index=['c1'], columns=['c2']))
print(df.pivot_table(['c3', 'c4'], index=['c1'], columns=['c2']))
print(df.pivot_table(['c3', 'c4'], index=['c1'], columns=['c2'], margins=True))
print(df.pivot_table(['c3', 'c4'], index=['c1'], columns=['c2'], aggfunc=sum))
print(df.pivot_table(['c3', 'c4'], index=['c1'], columns=['c2'], fill_value=0))

print(pd.crosstab(df.c1, df.c2))
print(pd.crosstab(df.c1, df.c2, values=df.c3, aggfunc=sum, margins=True))
