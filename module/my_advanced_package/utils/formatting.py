"""Formatting utilities"""

def format_number(number, decimal_places=2):
    """Format a number to specified decimal places."""
    return f"{number:.{decimal_places}f}"

def format_list(items, separator=", "):
    """Convert list items to a string."""
    return separator.join(str(item) for item in items)