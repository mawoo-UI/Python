import os
import datetime

def create_note(file_path, content):
    # 메모를 생성하는 함수
    try:
        # 디렉토리가 없으면 생성
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(file_path, 'w') as file:
            file.write(content)
        
        print(f"Note saved: {file_path}")
        return True
    
    except Exception as e:
        print(f"Note saving error: {e}")
        return False

def read_note(file_path):
    # 메모를 읽는 함수
    try:
      with open(file_path, 'r') as file:
          content = file.read()
      
      print(f"\n--- {file_path} ---")
      print(content)
      return content
  
    except FileNotFoundError:
      print(f"Error: File {file_path} not found.")
      return None
    
    except Exception as e:
      print(f"Note reading error: {e}")
      return None

def list_notes(directory):
    # 디렉토리 내의 메모 목록을 표시하는 함수
    try:
        if not os.path.exists(directory):
          print(f"Error: Directory {directory} not found.")
          return []
        
        notes = []
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path) and filename.endswith('.txt'):
              modified_time = os.path.getmtime(file_path)
              modified_date = datetime.datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
              file_size = os.path.getsize(file_path)
              notes.append((filename, modified_date, file_size))
        
        return notes
    
    except Exception as e:
        print(f"Note listing error: {e}")
        return []

if __name__ == "__main__":
    print("==== Simple Notepad ====")
    notes_dir = "notes"
    
    # 노트 디렉토리가 없으면 생성
    if not os.path.exists(notes_dir):
      os.makedirs(notes_dir)
      print(f"Notes directory created: {notes_dir}")
    
    while True:
      print("\n1. Write new note")
      print("2. Read note")
      print("3. List notes")
      print("4. Exit")
      choice = input("Select: ")
        
      if choice == '1':
          file_name = input("Note filename (e.g., note.txt): ")
          if not file_name.endswith('.txt'):
              file_name += '.txt'
          
          file_path = os.path.join(notes_dir, file_name)
          
          print("Enter note content. Press Ctrl+D (Unix) or Ctrl+Z (Windows) on an empty line to finish.")
          lines = []
          
          try:
              while True:
                  line = input()
                  lines.append(line)
          except EOFError:
              pass
          
          content = '\n'.join(lines)
          create_note(file_path, content)
      
      elif choice == '2':
          file_name = input("Note filename to read: ")
          if not file_name.endswith('.txt'):
              file_name += '.txt'
          
          file_path = os.path.join(notes_dir, file_name)
          read_note(file_path)
      
      elif choice == '3':
          notes = list_notes(notes_dir)
          
          if notes:
              print("\n--- Notes List ---")
              print("{:<20} {:<20} {:<10}".format("Filename", "Modified Date", "Size(bytes)"))
              print("-" * 50)
              
              for note in notes:
                  print("{:<20} {:<20} {:<10}".format(note[0], note[1], note[2]))
          else:
              print("No notes found.")
      
      elif choice == '4':
          print("Exiting program.")
          break
      
      else:
          print("Invalid selection.")