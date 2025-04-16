import re
from datetime import datetime

def analyze_log_file(log_file, pattern=None, start_date=None, end_date=None):
  # 로그 파일 분석 함수
  try:
    # 날짜 변환
    if start_date:
      start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if end_date:
      end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    # 로그 파일 읽기
    with open(log_file, 'r') as file:
      log_entries = []
      date_pattern = r'\[(\d{4}-\d{2}-\d{2})'  # [YYYY-MM-DD] 형식 찾기
      
      line_count = 0
      match_count = 0
      
      for line in file:
        line_count += 1
        match = True
        
        # 패턴 검사
        if pattern and pattern.lower() not in line.lower():
          match = False
        
        # 날짜 검사
        if (start_date or end_date) and match:
          date_match = re.search(date_pattern, line)
          if date_match:
            log_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
            if (start_date and log_date < start_date) or (end_date and log_date > end_date):
              match = False
        
        if match:
          log_entries.append(line)
          match_count += 1
      
      return {
        "total_lines": line_count,
        "matching_lines": match_count,
        "entries": log_entries
      }
  
  except FileNotFoundError:
    print(f"Error: Log file {log_file} not found.")
    return None
  except Exception as e:
    print(f"Error analyzing log file: {e}")
    return None

def display_log_analysis(result, max_entries=None):
  # 로그 분석 결과 표시 함수
  if not result:
    return
  
  print(f"\nLog Analysis Results:")
  print(f"Total lines processed: {result['total_lines']}")
  print(f"Matching entries found: {result['matching_lines']}")
  
  if result['entries']:
    print("\n--- Matching Log Entries ---")
    entries_to_show = result['entries'][:max_entries] if max_entries else result['entries']
    for entry in entries_to_show:
      print(entry.strip())
    
    if max_entries and len(result['entries']) > max_entries:
      print(f"\n... and {len(result['entries']) - max_entries} more entries")

if __name__ == "__main__":
  print("==== Log File Analyzer ====")
  
  log_file = input("Enter log file path: ")
  pattern = input("Search pattern (optional): ")
  start_date = input("Start date (YYYY-MM-DD, optional): ")
  end_date = input("End date (YYYY-MM-DD, optional): ")
  
  result = analyze_log_file(log_file, pattern, start_date, end_date)
  if result:
    display_log_analysis(result, max_entries=20)