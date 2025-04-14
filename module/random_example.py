# random 모듈 - 난수 생성
import random

# 난수 생성
print(f"0~1 between random number: {random.random()}")
print(f"1~100 between integer: {random.randint(1, 100)}")

# 리스트에서 랜덤 선택
fruits = ['apple', 'banana', 'stroberry', 'grape', 'orange']
print(f"random fruits: {random.choice(fruits)}")
print(f"choose 3 fruits: {random.sample(fruits, 3)}")

# 리스트 섞기
random.shuffle(fruits)
print(f"mixing fruits list: {fruits}")