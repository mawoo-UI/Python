import os
import shutil
import time

def copy_binary_file(source, destination, buffer_size=1024*1024):
    # 바이너리 파일을 버퍼 크기로 나누어 복사하는 함수
    # buffer_size: 한 번에 복사할 버퍼 크기 (기본값: 1MB)
    if not os.path.exists(source):
        print(f"Error: File {source} not found.")
        return False
    
    # 대상 디렉토리가 없으면 생성
    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    try:
        file_size = os.path.getsize(source)
        copied = 0
        start_time = time.time()
        
        with open(source, 'rb') as src_file:
            with open(destination, 'wb') as dst_file:
                while True:
                    buffer = src_file.read(buffer_size)
                    if not buffer:
                        break
                    
                    dst_file.write(buffer)
                    copied += len(buffer)
                    
                    # 진행률 표시
                    progress = (copied / file_size) * 100
                    elapsed_time = time.time() - start_time
                    speed = copied / (elapsed_time or 0.01) / (1024*1024)  # MB/s
                    
                    print(f"\rCopying: {progress:.1f}% ({copied}/{file_size} bytes) - {speed:.2f} MB/s", end='')
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\nCopy complete: {source} -> {destination}")
        print(f"File size: {file_size} bytes")
        print(f"Time taken: {duration:.2f} seconds")
        print(f"Average speed: {(file_size / (duration or 0.01) / (1024*1024)):.2f} MB/s")
        
        return True
    
    except Exception as e:
        print(f"\nFile copy error: {e}")
        return False

def fast_copy_binary_file(source, destination):
    # shutil.copy2를 사용한 빠른 복사 함수
    try:
        start_time = time.time()
        
        # 대상 디렉토리가 없으면 생성
        dest_dir = os.path.dirname(destination)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # 파일 복사
        shutil.copy2(source, destination)
        
        end_time = time.time()
        duration = end_time - start_time
        file_size = os.path.getsize(source)
        
        print(f"Copy complete: {source} -> {destination}")
        print(f"File size: {file_size} bytes")
        print(f"Time taken: {duration:.2f} seconds")
        print(f"Average speed: {(file_size / (duration or 0.01) / (1024*1024)):.2f} MB/s")
        
        return True
    
    except Exception as e:
        print(f"File copy error: {e}")
        return False

if __name__ == "__main__":
    print("==== Binary File Copy Program ====")
    
    while True:
        print("\n1. Standard copy (with progress)")
        print("2. Fast copy (using shutil)")
        print("3. Exit")
        choice = input("Select: ")
        
        if choice == '3':
            print("Exiting program.")
            break
        
        source = input("Source file path: ")
        destination = input("Destination file path: ")
        
        if choice == '1':
            buffer_size = input("Buffer size (MB, default: 1): ")
            try:
                buffer_size = int(buffer_size) * 1024 * 1024 if buffer_size else 1024*1024
            except ValueError:
                buffer_size = 1024*1024
                print("Invalid buffer size, using default 1MB.")
            
            copy_binary_file(source, destination, buffer_size)
        
        elif choice == '2':
            fast_copy_binary_file(source, destination)
        
        else:
            print("Invalid selection.")