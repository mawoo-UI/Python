"""Validation utilities"""
import sys
import os
# 패키지 루트 디렉토리를 sys.path에 추가
package_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, package_root)

# 이제 패키지를 절대 경로로 임포트할 수 있습니다
from my_advanced_package.config import MAX_ITEMS

def validate_input(data):
    """Validate input data."""
    if not data:
        return False, "Data is empty."
    
    if len(data) > MAX_ITEMS:
        return False, f"Too many data items. Maximum {MAX_ITEMS} allowed."
    
    return True, "Data is valid."