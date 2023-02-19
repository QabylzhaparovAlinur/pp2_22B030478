from datetime import *

# 1
# today = date.today()
# print(today)
# minus5 = timedelta(days=5)
# print(today - minus5)

# 2
# today = date.today()
# yesterday = today - timedelta(days=1)
# tomorrow = today + timedelta(days=1)
# print(yesterday)
# print(today)
# print(tomorrow)

# 3
# now = datetime.now()
# print(now)
# now = now.replace(microsecond=0)
# print(now)

# 4
# date1 = datetime(year=2023, month=2, day=20, hour=17)
# date2 = datetime(year=2023, month=4, day=2, hour=7)
# difference = date2 - date1 
# '''d, hh:mm:ss'''
# secondsDifference = difference.total_seconds()
# print(secondsDifference)