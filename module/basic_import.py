# 기본 모듈 가져오기
import my_module

# 모듈 변수 사용
print(my_module.name)             # 출력: Python 모듈 시스템
print(my_module.version)          # 출력: 3.10

# 모듈 함수 사용
print(my_module.greet("rona"))   # 출력: 안녕하세요, 홍길동님!
print(my_module.add(10, 5))       # 출력: 15

# 모듈 클래스 사용
calc = my_module.Calculator("MyCalculatingMachine")
print(calc.name)                  # 출력: 내 계산기
print(calc.multiply(3, 4))        # 출력: 12
print(calc.divide(10, 2))         # 출력: 5.0