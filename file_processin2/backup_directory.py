import os
import shutil
import datetime

def backup_directory(source_dir, backup_dir=None):
  # 디렉토리 백업 함수
  try:
    # 소스 디렉토리 확인
    if not os.path.exists(source_dir):
      print(f"Error: Source directory {source_dir} not found.")
      return False
    
    # 백업 디렉토리가 지정되지 않은 경우 자동 생성
    if backup_dir is None:
      timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
      backup_dir = f"{source_dir}_backup_{timestamp}"
    
    # 백업 디렉토리 생성
    if not os.path.exists(backup_dir):
      os.makedirs(backup_dir)
      print(f"Backup directory created: {backup_dir}")
    
    # 파일 복사
    file_count = 0
    for root, dirs, files in os.walk(source_dir):
      # 상대 경로 계산
      rel_path = os.path.relpath(root, source_dir)
      # 대상 디렉토리 생성
      target_dir = os.path.join(backup_dir, rel_path) if rel_path != '.' else backup_dir
      if not os.path.exists(target_dir):
        os.makedirs(target_dir)
      
      # 파일 복사
      for file in files:
        source_file = os.path.join(root, file)
        target_file = os.path.join(target_dir, file)
        shutil.copy2(source_file, target_file)
        file_count += 1
        print(f"Copied: {source_file} -> {target_file}")
    
    print(f"\nBackup complete! {file_count} files copied to {backup_dir}")
    return True
  
  except Exception as e:
    print(f"Backup error: {e}")
    return False

if __name__ == "__main__":
  source_dir = input("Enter source directory to backup: ")
  backup_dir = input("Enter backup directory (leave empty for auto-generated): ")
  
  if not backup_dir:
    backup_dir = None
  
  backup_directory(source_dir, backup_dir)