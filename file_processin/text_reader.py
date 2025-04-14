def read_file(file_path):
    # 파일의 전체 내용을 읽는 함수
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"File reading error: {e}")
        return None

def read_file_lines(file_path):
    # 파일을 줄 단위로 읽는 함수
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # 줄바꿈 문자 제거
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except Exception as e:
        print(f"File reading error: {e}")
        return []

if __name__ == "__main__":
    file_path = input("Enter file path to read: ")
    
    # 전체 내용 읽기
    print("\n--- Entire File Content ---")
    content = read_file(file_path)
    if content:
        print(content)
    
    # 줄 단위로 읽기
    print("\n--- Line by Line Content ---")
    lines = read_file_lines(file_path)
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line}")