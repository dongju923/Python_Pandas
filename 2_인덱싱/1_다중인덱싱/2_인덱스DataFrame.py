import numpy as np
import pandas as pd

korea_pop_df = pd.DataFrame({'인구수': [9720846, 3404423, 2947217, 2427954, 1471040, 1455048], '남자인구수': [4732275, 1668618, 1476813, 1198815, 734441, 720060], '여자인구수': [
                            4988571, 1735805, 1470404, 1229139, 736599, 734988]}, index=["서울특별시", "부산광역시", "인천광역시", "대구광역시", "대전광역시", "광주광역시"])
korea_pop_df["남여비율"] = (korea_pop_df.남자인구수 / korea_pop_df.여자인구수) * 100
print(korea_pop_df)

# 멀티인덱스에 사용할 인덱스 생성
idx_tuples = [('서울특별시', 2010), ('서울특별시', 2020),
              ('부산광역시', 2010), ('부산광역시', 2020),
              ('인천광역시', 2010), ('인천광역시', 2020),
              ('대구광역시', 2010), ('대구광역시', 2020),
              ('대전광역시', 2010), ('대전광역시', 2020),
              ('광주광역시', 2010), ('광주광역시', 2020)]
print(idx_tuples)

# 멀티인덱스에 사용할 값 생성
pop_tuples = [10312545, 9720846, 2567910, 3404423, 2758296,
              2947217, 2511676, 2427954, 1503664, 1471040, 1454636, 1455048]

# Series객체로 변환
population = pd.Series(pop_tuples, index=idx_tuples)
print(population)

# 멀티인덱스 변환
midx = pd.MultiIndex.from_tuples(idx_tuples)
print(midx)

# 변환된 멀티인덱스로 다시 재인덱스
population = population.reindex(midx)
print(population)

# 인덱싱
print(population[:, 2010])
print(population[:, 2020])
print(population['부산광역시', :])

# Series객체를 DataFrame 구조로 변환
korea_mdf = population.unstack()
print(korea_mdf)

# DataFrame을 다중인덱스 구조로 변환
print(korea_mdf.stack())

# 남자인구 값 생성
male_tuples = [5111259, 4732275, 1773170, 1668618, 1390356,
               1476813, 1255245, 1198815, 753648, 734441, 721780, 720060]
print(male_tuples)

# DataFrame생성
korea_mdf = pd.DataFrame({"총인구수": population, "남자인구수": male_tuples})
print(korea_mdf)
