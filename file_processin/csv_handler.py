import csv
import os

def read_csv(file_path, delimiter=','):
  try:
    data = []
    with open(file_path, 'r', newline='') as file:
      csv_reader = csv.reader(file, delimiter=delimiter)
      for row in csv_reader:
        data.append(row)
    
    print(f"CSV file read successfully: {len(data)} rows")
    return data
  
  except FileExistsError:
    print(f"Error: File {file_path} not found.")
    return []

  except Exception as e:
    print(f"CSV reading error: {e}")
    return []

def write_csv(file_path, data, delimiter=','):
  try:
    with open(file_path, 'w', newline='') as file:
      csv_writer = csv.writer(file, delimiter=delimiter)
    
    print(f"CSV file saved successfully: {file_path} ({len(data)} rows)")
    return True
  
  except Exception as e:
    print(f"CSV writing error: {e}")
    return False

def display_csv(data):
  if not data:
    print("No data to display.")
    return
  
  col_widths = []
  for i in range(len(data[0])):
    width =max(len(str(row[i])) for row in data if i < len(row))
    col_widths.append(width)

  #헤더
  header = data[0]
  header_line = "|".join(str(header[i]).ljust(col_widths[i]) for i in range(len(header)))
  print(header_line)
  print("-" * len(header_line))

  #데이터 출력
  for row in data[1:]:
    row_line = "|".join(str(row[i]).ljust(col_widths[i]) if i < len(row) else "".ljust(col_widths[i]) for i in range(len(header)))
    print(row_line)
if __name__ == "__main__":
  print("=== CSV File Handler ===")

  while True:
    print("\n1. Read CSV file")
    print("2. Create CSV file")
    print("3. Exit")
    choice = input("Select: ")

    if choice == '1':
      file_path = input("CSV file path to read: ")
      delimiter = input("Delimiter (default: comma): ") or ','
      data = read_csv(file_path, delimiter)
      if data:
        display_csv(data)

    elif choice == '2':
      file_path = input("CSV file path to read: ")
      delimiter = input("Delimiter (default: comma): ") or ','

      print("Enter data. Separate values with commas. Press Enter on an empty line to finish.")
      data = []
    
      while True:
        line = input()
        if not line:
          break
        row = [item.strip() for item in line.split(',')]
        data.append(row)

      if data:
        write_csv(file_path, data, delimiter)
  
    elif choice == '3':
      print("Exiting program.")
      break
    
    else:
      print("Invalid selection.")