import my_advanced_package
from my_advanced_package.utils.formatting import format_number, format_list

print(f"Package version: {my_advanced_package.__version__}")

data = [1, 2, 3, 4, 5]
result = my_advanced_package.process_data(data, user_id=42)
print(f"Processing result: {result}")

print(f"Number formatting: {format_number(3.14159, 3)}")
print(f"List formatting: {format_list(['apple', 'banana', 'orange'])}")

from my_advanced_package.config import DEFAULT_LANGUAGE
print(f"Default language: {DEFAULT_LANGUAGE}")