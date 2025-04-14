"""This module is for practicing special variables and attribute exploration."""

# Define public items only
__all__ = ['add', 'multiply', 'PUBLIC_VALUE']

# Constants
PUBLIC_VALUE = 100
_PRIVATE_VALUE = 200  # Conventionally considered private with _ prefix

# Functions
def add(a, b):
    """Adds two numbers."""
    return a + b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def _private_function():
    """This function is considered private."""
    return "This function is for internal use only."

# Module execution check
if __name__ == "__main__":
    print("This module is being executed directly.")
else:
    print("This module has been imported.")