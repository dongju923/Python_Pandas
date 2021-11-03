"""
get(): 각 요소에 인덱스 지정
slice(): 각 요소에 슬라이스 적용
slice_replace(): 각 요소의 슬라이스를 특정 값으로 대체
cat(): 문자열 연결
repeat(): 값 반복
normalize(): 문자열의 유니코드 형태로 변환
pad(): 문자열의 양쪽 공백 추가
lpad(): 문자열의 왼쪽 공백 추가
rpad(): 문자열의 오른쪽 공백 추가
wrap(): 긴 문자열을 주어진 너비보다 짧은 길이의 여러줄로 나눔
join(): Series의 각 요소에 있는 문자열을 전달된 구분자와 결합
get_dummies(): DataFrame으로 가변수 추출
"""
import pandas as pd
import numpy as np

name_tuple = ["Dong Ju", "Steven Jobs", "Larry Page", "Elon Musk",
              "Bill Gates", "Mark Zuckerberg", None, "Jeff Bezos"]
names = pd.Series(name_tuple)
print(names)

print(names.str.slice(0, 4))
print(names.str[0:4])

print(names.str.split().str.get(-1))

print(names.str.repeat(2))

print(names.str.join('_'))
