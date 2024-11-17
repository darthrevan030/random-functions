from datetime import datetime

now = datetime.now()

time_str = now.strftime("%H:%M:%S")
date_str = now.strftime("%Y-%m-%d")

print(f"Today is {date_str} and it is {time_str}.")
