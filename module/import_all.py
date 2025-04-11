# 모든 항목 가져오기 (*는 주의해서 사용해야 함)
from my_module import *

# 모든 항목을 직접 사용 가능
print(name)                # 출력: Python 모듈 시스템
print(version)             # 출력: 3.10
print(greet("lord"))     # 출력: 안녕하세요, 이영수님!
print(add(8, 7))           # 출력: 15

calc = Calculator("Star Calculator")
print(calc.multiply(9, 9)) # 출력: 81