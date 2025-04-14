import os
import datetime
import shutil

def get_size_format(size):
  # 파일 크기를 읽기 쉬운 형식으로 변환
  for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
    if size < 1024:
        return f"{size:.2f} {unit}"
    size /= 1024
  return f"{size:.2f} PB"

def get_file_info(file_path):
  # 파일 정보를 가져오는 함수
  try:
    stats = os.stat(file_path)
    file_size = stats.st_size
    modified_time = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    access_time = datetime.datetime.fromtimestamp(stats.st_atime).strftime('%Y-%m-%d %H:%M:%S')
    creation_time = datetime.datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
      
    return {
      "size": file_size,
      "size_formatted": get_size_format(file_size),
      "modified": modified_time,
      "accessed": access_time,
      "created": creation_time,
      "is_file": os.path.isfile(file_path)
    }
  except Exception as e:
    print(f"Error getting file info: {e}")
    return None

def list_directory(directory):
  # 디렉토리 내용을 나열하는 함수
  try:
    if not os.path.exists(directory):
      print(f"Error: Directory {directory} not found.")
      return None
    
    if not os.path.isdir(directory):
      print(f"Error: {directory} is not a directory.")
      return None
    
    items = []
    total_size = 0
    file_count = 0
    dir_count = 0
      
    for item in os.listdir(directory):
      path = os.path.join(directory, item)
      info = get_file_info(path)
        
      if info:
        items.append({
            "name": item,
            "path": path,
            "info": info
        })
        
        if info["is_file"]:
            total_size += info["size"]
            file_count += 1
        else:
            dir_count += 1
      
    # 항목 정렬 (디렉토리 먼저, 그 다음 파일)
    items.sort(key=lambda x: (x["info"]["is_file"], x["name"].lower()))
    
    return {
      "items": items,
      "total_size": total_size,
      "total_size_formatted": get_size_format(total_size),
      "file_count": file_count,
      "dir_count": dir_count
    }
  
  except Exception as e:
    print(f"Error listing directory: {e}")
    return None

def display_directory(directory_info):
    # 디렉토리 내용을 표시하는 함수
    if not directory_info:
      return
    
    items = directory_info["items"]
    
    print("\n{:<30} {:<10} {:<20} {:<5}".format("Name", "Size", "Modified", "Type"))
    print("-" * 70)
    
    for item in items:
      info = item["info"]
      item_type = "DIR" if not info["is_file"] else "FILE"
      size = info["size_formatted"] if info["is_file"] else "<DIR>"
      
      print("{:<30} {:<10} {:<20} {:<5}".format(
        item["name"][:29], size, info["modified"], item_type
      ))
    
    print("-" * 70)
    print(f"Total: {directory_info['file_count']} files, {directory_info['dir_count']} directories")
    print(f"Total size: {directory_info['total_size_formatted']}")

if __name__ == "__main__":
    print("==== File Browser ====")
    
    current_dir = os.getcwd()
    
    while True:
      print(f"\nCurrent directory: {current_dir}")
      print("\n1. List current directory")
      print("2. Navigate to parent directory")
      print("3. Navigate into directory")
      print("4. Show file details")
      print("5. Exit")
      choice = input("Select: ")
        
      if choice == '1':
        dir_info = list_directory(current_dir)
        display_directory(dir_info)
      
      elif choice == '2':
        parent_dir = os.path.dirname(current_dir)
        if parent_dir and parent_dir != current_dir:
            current_dir = parent_dir
        else:
          print("Already at root directory.")
        
      elif choice == '3':
        dir_name = input("Enter directory name: ")
        new_dir = os.path.join(current_dir, dir_name)
        
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
          current_dir = new_dir
        else:
          print(f"Directory {dir_name} does not exist.")
      
      elif choice == '4':
        file_name = input("Enter file name: ")
        file_path = os.path.join(current_dir, file_name)
        
        if os.path.exists(file_path):
          info = get_file_info(file_path)
          
          if info:
            print("\n--- File Details ---")
            print(f"Name: {file_name}")
            print(f"Path: {file_path}")
            print(f"Size: {info['size_formatted']} ({info['size']} bytes)")
            print(f"Type: {'File' if info['is_file'] else 'Directory'}")
            print(f"Modified: {info['modified']}")
            print(f"Accessed: {info['accessed']}")
            print(f"Created: {info['created']}")
        else:
          print(f"File {file_name} does not exist.")
        
      elif choice == '5':
        print("Exiting program.")
        break
    
      else:
        print("Invalid selection.")