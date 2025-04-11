# 변수 정의
name = "Python module system"
version = 3.10

# 함수 정의
def greet(person):
    return f"Hello, {person} sir!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 클래스 정의
class Calculator:
    def __init__(self, name="basicCalculator"):
        self.name = name
        
    def multiply(self, a, b):
        return a * b
        
    def divide(self, a, b):
        if b == 0:
            return "Cannot be divided by 0."
        return a / b
    def power(self, a, b):
        return a ** b