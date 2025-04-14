import os
import shutil

def copy_file(source, destination):
  try:
    if not os.path.exists(source):
      print(f"Error: File {source} not found.")
      return False
    
    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
      os.makedirs(dest_dir)
      print(f"Directory created: {dest_dir}")

    shutil.copy2(source, destination)
    print(f"File {source} copied to {destination}.")
    return True
  
  except Exception as e:
    print(f"File copy error: {e}")
    return False

def copy_multiple_files(sources, destination_dir):
  if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
    print(f"Directory created: {destination_dir}")
  
  success_count = 0
  for source in sources:
    dest_file = os.path.join(destination_dir, os.path.basename(source))
    if copy_file(source, dest_file):
      success_count += 1
    
  print(f"Total {success_count} of {len(sources)} files copied successfully")
  return success_count

if __name__ == "__main__":
  print("=== File Copy Program ===")

  source = input("Source file path: ")
  destination = input("Destination file path: ")
  copy_file(source, destination)

  print("\nMultiple File Copy")
  print("Enter file paths one by one. Press Enter on an empty line to finish.")

  sources = []
  while True:
    source = input("File path to copy (press Enter to finish): ")
    if not source:
      break
    sources.append(source)

  if sources:
    destination_dir = input("Destination directory: ")
    copy_multiple_files(sources, destination_dir)