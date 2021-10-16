import numpy as np
import pandas as pd

korea_pop_df = pd.DataFrame({'인구수': [9720846, 3404423, 2947217, 2427954, 1471040, 1455048], '남자인구수': [4732275, 1668618, 1476813, 1198815, 734441, 720060], '여자인구수': [
                            4988571, 1735805, 1470404, 1229139, 736599, 734988]}, index=["서울특별시", "부산광역시", "인천광역시", "대구광역시", "대전광역시", "광주광역시"])
print(korea_pop_df)

# 인덱스, 칼럼, 값 반환
print(korea_pop_df.index)
print(korea_pop_df.columns)
print(korea_pop_df.values)

# 칼럼과 값 반환
print(korea_pop_df["남자인구수"])
print(korea_pop_df.남자인구수)
print(korea_pop_df.여자인구수)

# 칼럼 추가
korea_pop_df["남여비율"] = (korea_pop_df.남자인구수 / korea_pop_df.여자인구수) * 100
print(korea_pop_df.남여비율)

# 인덱스와 칼럼 위치 바꿈
print(korea_pop_df.T)

# 특정 값만 반환
print(korea_pop_df.values[0])
# 서울특별시
print(korea_pop_df.values[1])
# 부산광역시

# 특정 인덱스와 값 반환
print(korea_pop_df.loc["서울특별시"])
print(korea_pop_df.loc["광주광역시"])

# 인덱스 슬라이싱
print(korea_pop_df["서울특별시":"인천광역시"])
print(korea_pop_df.loc["서울특별시":"인천광역시"])

# 인덱스, 칼럼 동시 슬라이싱
print(korea_pop_df.loc[:"인천광역시", :"남자인구수"])
print(korea_pop_df.loc["부산광역시":"대전광역시", "남자인구수":"여자인구수"])

# 특정 조건 DataFrame반환
print(korea_pop_df[(korea_pop_df.여자인구수 > 1500000)])
print(korea_pop_df.loc[(korea_pop_df.여자인구수 > 1500000)])

print(korea_pop_df[(korea_pop_df.인구수 > 2500000) & (korea_pop_df.남여비율 > 100)])
print(korea_pop_df.loc[(korea_pop_df.인구수 > 2500000)
      & (korea_pop_df.남여비율 > 100)])

# 인덱스 위치로 인덱스 찾기
print(korea_pop_df.iloc[1])
print(korea_pop_df.iloc[:3, :2])
