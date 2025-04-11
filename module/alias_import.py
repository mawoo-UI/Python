# 별칭 사용하기
# 모듈에 별칭 지정
import my_module as mm

print(mm.name)              # 출력: Python 모듈 시스템
print(mm.add(20, 30))       # 출력: 50

# 특정 항목에 별칭 지정
from my_module import Calculator as Calc, greet as say_hello

my_calc = Calc("simple CalculatingMachine")
print(my_calc.name)              # 출력: 간단 계산기
print(say_hello("Emotab"))       # 출력: 안녕하세요, 박영희님!