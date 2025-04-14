# Check the effect of __all__ when using from module import *
from advanced_module import *

print(f"PUBLIC_VALUE: {PUBLIC_VALUE}")
print(f"add(3, 4): {add(3, 4)}")
print(f"multiply(5, 6): {multiply(5, 6)}")

# The following line would cause an error - not included in __all__
# print(_PRIVATE_VALUE)  # NameError: name '_PRIVATE_VALUE' is not defined