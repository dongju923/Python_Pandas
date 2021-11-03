"""문자열 연산자
str.capitalize()
str.casefold()
str.count()
str.find()
str.rfind()
str.index())
str.rindex()
str.isalnum()
str.isalpha()
str.isdecimal()
str.isdigit()
str.isnumeric()
str.isidentifier()
str.isspace()
str.istitle()
str.islower()
str.isupper()
str.join()
str.center()
str.ljust()
str.rjust()
str.lower()
str.upper()
str.swapcase()
str.strip([chars])
str.lstrip([chars])
str.rstrip([chars])
str.partition(sep)
str.repartition(sep)
str.replace()
str.split()
str.rsplit()
str.splitlines()
str.startswith()
str.endswith()
str.zfill()
"""
import pandas as pd
import numpy as np

# 튜플을 Series형태로 만듦
name_tuple = ["Dong Ju", "Steven Jobs", "Larry Page", "Elon Musk",
              "Bill Gates", "Mark Zuckerberg", None, "Jeff Bezos"]
names = pd.Series(name_tuple)
print(names)

# 전부 소문자
print(names.str.lower())

# 앞글자만 대문자
print(names.str.capitalize())

# 전부 대문자
print(names.str.upper())

# 길이 반환
print(names.str.len())

# 띄어쓰기를 기준으로 문자열을 자르고 리스트로 반환
print(names.str.split())
