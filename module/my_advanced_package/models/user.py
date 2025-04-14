"""User model"""
import sys
import os

# 패키지 루트 디렉토리를 sys.path에 추가
package_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, package_root)

class User:
    """Class for storing user information"""
    
    def __init__(self, id, name, email=None):
        self.id = id
        self.name = name
        self.email = email
    
    def __str__(self):
        if self.email:
            return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
        return f"User(id={self.id}, name='{self.name}')"