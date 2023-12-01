# Formatting dates

from datetime import datetime

date = datetime.strptime('2023-11-20 8:28:23', '%Y-%m-%d %H:%M:%S')
print(date.strftime('%m/%d/%Y %H:%M'))
print(date.strftime('%m/%d/%Y'))
