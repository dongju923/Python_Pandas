import pandas as pd
import numpy as np

print(pd.__version__)
# 판다스 버전 출력

# 관계 또는 레이블링 데이터로 쉽고 직관적으로 작업할 수 있도록 고안된 빠르고 유연하며 표현력이 뛰어난 데이터 구조를 제공하는 Python 패키지

### Pandas특징 ###
# 부동 소수점이 아닌 데이터 뿐만 아니라 부동 소수점 테이터에서도 결측 테이터(NAN)를 쉽게 처리
# 크기 변이성(Size mutability): DataFrame및 고차원 객체에서 열을 삽입 및 삭제 가능
# 자동 및 명시적 데이터 정렬: 객체를 라벨 집합에 명시적으로 정렬하거나, 사용자가 라벨을 무시하고 Series, DataFrame등의 계산에서 자동으로 데이터 조정 가능
# 데이터 세트에서 집계 및 변환을 위한 분할, 적용, 결합 작업을 수행할 수 있는 강력하고 유연한 group-by함수 제공
# 누락된 데이터 또는 다른 Python 및 Numpy데이터 구조에서 서로 다른 인덱싱 데이터를 DataFrame 개체로 쉽게 변환
# 대용량 데이터 세트의 지능형 라벨 기반 슬라이싱, 고급 인덱싱 및 부분 집합 구하기 가능
# 직관적인 데이터 세트 병합 및 결함
# 데이터 세트의 유연한 재구성 및 피벗
# 측의 계층적 라벨링
# 플랫파일(csv), Excel파일, 데이터베이스 로딩 및 초고속 HDF5 형식의 데이터 저장/로드에 사용되는 강력한 도구
# 시계열 특정 기능: 날짜 범위 생성 및 주파수 변환, 무빙 윈도우 통계, 날짜 이동 및 지연
