# 패키지 사용하기
import my_package
print(my_package.__version__)  # 출력: 1.0.0

# 패키지 내 모듈 가져오기
from my_package import math_utils

# 모듈 사용
print(math_utils.PI)  # 출력: 3.14159
print(math_utils.add(5, 3))  # 출력: 8

# 모듈 내 클래스 사용
print(math_utils.MathUtility.square(4))  # 출력: 16