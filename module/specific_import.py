# 특정 항목만 가져오기
from my_module import greet, Calculator

# 가져온 함수 직접 사용 (모듈 이름 없이)
print(greet("Porori"))  # 출력: 안녕하세요, 김철수님!

# 가져온 클래스 직접 사용
my_calc = Calculator("advanced CalculatingMachine")
print(my_calc.name)            # 출력: 고급 계산기
print(my_calc.multiply(5, 6))  # 출력: 30

# 주의: version은 가져오지 않았으므로 사용 불가
# print(version)  # 오류 발생: NameError: name 'version' is not defined