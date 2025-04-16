def analyze_text_file(file_path):

  try:
    with open(file_path, 'r') as file:
      content = file.read()
      lines = content.split('\n')
      words = content.split()
      chars = len(content)

      print(f"File statistics for: {file_path}")
      print(f"Lines: {len(lines)}")
      print(f"Words: {len(words)}")
      print(f"Characters: {chars}")

      word_count = {}
      for word in words:
        word = word.lower().strip('.,!?;:()"\'')
        if word:
          word_count[word] = word_count.get(word, 0) + 1

      top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
      print("\nTop 5 words:")
      for word, count in top_words:
        print(f"{word}: {count} times")

      return True
  except FileNotFoundError:
    print(f"Error: File {file_path} not found.")
    return False
  
  except Exception as e:
    print(f"Error analyzing file: {e}")
    return False
if __name__ == "__main__":
  file_path = input("Enter text file path to analyze: ")
  analyze_text_file(file_path)