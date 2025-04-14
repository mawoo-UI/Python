def write_file(file_path, content, mode='w'):
  try:
    with open(file_path, mode) as file:
      file.write(content)
    print(f"File successfully saved: {file_path}")
    return True
  except Exception as e:
    print(f"file writing error: {e}")
    return False
def write_lines(file_path, lines, mode='w'):
  try:
    with open(file_path, mode) as file:
      for line in lines:
        file.write(line + '\n')
        print(f"File successfully saved: {file_path}")
        return True
  except Exception as e:
    print(f"File writing error: {e}")
    return False
if __name__ == "__main__":
  file_path = input("Enterfile path to save: ")

  content = input("Enter content to save to file: ")
  write_file(file_path, content)

  lines_file = input("Enter file path for multiple lines: ")
  print("Enter multiple lines. Press Enter on an empty line to finish.")

  lines = []
  while True:
    line = input()
    if not line:
      break
    lines.append(line)
  
  write_lines(lines_file, lines)