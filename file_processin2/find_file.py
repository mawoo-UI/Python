import os
import fnmatch
import time

def find_files(directory, pattern, size_limit=None, modified_days=None):
  # 파일 찾기 함수
  try:
    if not os.path.exists(directory):
      print(f"Error: Directory {directory} not found.")
      return []
    
    found_files = []
    current_time = time.time()
    
    for root, dirs, files in os.walk(directory):
      for filename in files:
        if fnmatch.fnmatch(filename.lower(), pattern.lower()):
          file_path = os.path.join(root, filename)
          file_size = os.path.getsize(file_path)
          modified_time = os.path.getmtime(file_path)
          days_old = (current_time - modified_time) / (60 * 60 * 24)
          
          # 크기 제한 검사
          if size_limit is not None and file_size > size_limit:
            continue
          
          # 수정 날짜 검사
          if modified_days is not None and days_old > modified_days:
            continue
          
          found_files.append({
            "path": file_path,
            "size": file_size,
            "modified": time.ctime(modified_time),
            "days_old": days_old
          })
    
    return found_files
  
  except Exception as e:
    print(f"Error searching files: {e}")
    return []

def display_results(files):
  # 검색 결과 표시 함수
  if not files:
    print("No files found matching your criteria.")
    return
  
  print(f"\nFound {len(files)} matching files:")
  print("{:<60} {:<10} {:<25}".format("Path", "Size (KB)", "Modified"))
  print("-" * 95)
  
  for file in files:
    size_kb = file["size"] / 1024
    print("{:<60} {:<10.2f} {:<25}".format(
      file["path"][:60], size_kb, file["modified"]
    ))

if __name__ == "__main__":
  directory = input("Enter directory to search: ")
  pattern = input("Enter file pattern (e.g. *.txt, doc*.docx): ")
  
  size_input = input("Maximum file size in KB (optional): ")
  size_limit = float(size_input) * 1024 if size_input else None
  
  days_input = input("Modified within days (optional): ")
  modified_days = float(days_input) if days_input else None
  
  found_files = find_files(directory, pattern, size_limit, modified_days)
  display_results(found_files)