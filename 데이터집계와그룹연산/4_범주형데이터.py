"""범주형 데이터 함수
add_categories: 기존 카테고리에 새로운 카테고리 추가
as_ordered: 카테고리에 순서 지정
as_unordered: 카테고리에 순서 미지정
remove_categories: 카테고리 제거
remove_unused_categories: 사용안하는 카테고리 제거
rename_catagories: 카테고리 이름 변경
reorder_categories: 새로운 카테고리에 순서 지정
set_categories: 새로운 카테고리로 변경
"""
import pandas as pd
import numpy as np

s = pd.Series(['c1', 'c2', 'c1', 'c2', 'c1']*2)
print(s)

print(pd.unique(s))
# 고유값 반환
print(pd.value_counts(s))
# 값 개수 반환

code = pd.Series([0, 1, 0, 1, 0]*2)
print(code)

d = pd.Series(['c1', 'c2'])
print(d)

print(d.take(code))
# c1=0, c2=1로 매핑되어서 반환

df = pd.DataFrame({'id': np.arange(len(s)), 'c': s,
                  'v': np.random.randint(1000, 5000, size=len(s))})
print(df)

c = df['c'].astype('category')
# dtype: category로 변환

print(c.values)
print(c.values.categories)
print(c.values.codes)

c = pd.Categorical(['c1', 'c2', 'c3', 'c1', 'c2'])
# categorical 데이터로 변환

categories = ['c1', 'c2', 'c3']
codes = [0, 1, 2, 0, 1]
c = pd.Categorical.from_codes(codes, categories)
print(c)
# categorical데이터 만들기

print(pd.Categorical.from_codes(codes, categories, ordered=True))
# catagorical데이터에 순서지정
print(c.as_ordered())
# catagorical데이터에 순서지정
c = c.set_categories(['c1', 'c2', 'c3', 'c4', 'c5'])
print(c)
# 카테고리 추가
print(c.value_counts())
# 카테고리 value개수 반환

c = c.remove_unused_categories()
# 사용하지 않는 카테고리(c4,c5)삭제
print(c.categories)
