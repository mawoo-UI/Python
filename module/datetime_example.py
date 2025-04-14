# datetime 모듈 - 날짜 시간 처리
import datetime

now = datetime.datetime.now()
print(f"now: {now}")
print(f"formatted date: {now.strftime('%Yyear %mmonth %dday')}")

# 일주일 후 날짜 계산
one_week_later = now + datetime.timedelta(days=7)
print(f"one week later: {one_week_later.strftime('%Yyear %mmonth %dday')}")