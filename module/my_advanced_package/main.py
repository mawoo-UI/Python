"""Main functionality module"""
import sys
import os

# 패키지 루트 디렉토리를 sys.path에 추가
package_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, package_root)

from my_advanced_package.config import DEBUG
from my_advanced_package.utils.validation import validate_input
from my_advanced_package.models.user import User

def process_data(data, user_id=None):
    """Main function for processing data"""
    if DEBUG:
        print(f"Data processing started: {len(data)} items")
    
    # Input validation
    is_valid, message = validate_input(data)
    if not is_valid:
        return {"success": False, "error": message}
    
    # Get user info (if available)
    user = None
    if user_id:
        user = User(user_id, f"User{user_id}")
    
    # Data processing logic
    result = {"success": True, "processed_items": len(data)}
    
    if user:
        result["user"] = str(user)
    
    if DEBUG:
        print("Data processing completed")
    
    return result