"""File handling utility module"""

def read_file(filename):
    """Reads file content and returns it as a string."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File {filename} not found."
    except Exception as e:
        return f"Error: {str(e)}"

def write_file(filename, content):
    """Writes a string to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully saved to {filename} file."
    except Exception as e:
        return f"Error: {str(e)}"

def append_file(filename, content):
    """Appends a string to a file."""
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully appended to {filename} file."
    except Exception as e:
        return f"Error: {str(e)}"