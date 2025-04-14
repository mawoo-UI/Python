# Using the file module
from file_utils import write_file, read_file, append_file

# Write content to file
result = write_file('sample.txt', 'Hello!\nI am learning Python module system.\n')
print(result)

# Append content to file
result = append_file('sample.txt', 'I am also learning file I/O.\n')
print(result)

# Read file content
content = read_file('sample.txt')
print("\nFile content:")
print(content)