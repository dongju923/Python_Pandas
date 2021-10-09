import numpy as np
import pandas as pd

print(pd.DataFrame({'A': 2, 'B': 4, 'D': 3}, {'A': 4, 'B': 5, 'C': 7}))

print(pd.DataFrame([{'A': 2, 'B': 4, 'D': 3}, {'A': 4, 'B': 5, 'C': 7}]))

print(pd.DataFrame(np.random.rand(5, 5)))

print(pd.DataFrame(np.random.randint(1, 10, (5, 5)), columns=[
      'A', 'B', 'C', 'D', 'E'], index=[1, 2, 3, 4, 5]))

male_tuple = {"서울특별시": 4732275, "부산광역시": 1668618,
              "인천광역시": 1476813, "대구광역시": 1198815, "대전광역시": 734441}
male_pop = pd.Series(male_tuple)
print(male_pop)

female_tuple = {"서울특별시": 4988571, "부산광역시": 1735805,
                "인천광역시": 1470403, "대구광역시": 1229139, "광주광역시": 736599}
female_pop = pd.Series(female_tuple)
print(female_pop)

korea_pop_df = pd.DataFrame({"남자인구수": male_pop, "여자인구수": female_pop})
print(korea_pop_df)

print(korea_pop_df.index)
# 인덱스 객체 확인
print(korea_pop_df.columns)
# 컬럼 객체 확인
print(korea_pop_df["여자인구수"])
print(korea_pop_df["남자인구수"])
print(korea_pop_df["대구광역시":"부산광역시"])
