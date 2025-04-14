"""수학 유틸리티 함수 모듈"""

PI = 3.14159

def add(a, b):
    """두 수를 더합니다."""
    return a + b

def multiply(a, b):
    """두 수를 곱합니다."""
    return a * b

class MathUtility:
    """수학 유틸리티 클래스"""
    
    @staticmethod
    def square(x):
        """숫자의 제곱을 반환합니다."""
        return x * x