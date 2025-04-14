# Exploring module attributes
import advanced_module

# Module name
print(f"Module name: {advanced_module.__name__}")

# Module documentation string
print(f"Module doc: {advanced_module.__doc__}")

# List of attributes in the module
print("\nAll attributes in module:")
for name in dir(advanced_module):
    if not name.startswith('__'):  # Exclude special attributes
        print(f"- {name}")

# Access to private attributes (not recommended but possible)
print(f"\nPrivate value: {advanced_module._PRIVATE_VALUE}")
print(f"Private function call: {advanced_module._private_function()}")

# Access function docstring
print(f"\nFunction docstring: {advanced_module.add.__doc__}")