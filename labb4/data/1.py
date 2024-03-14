import datetime

x = datetime.datetime.now()
a = int(x.strftime("%d")) - 5
q = datetime.datetime(x.year, x.month, a, x.hour, x.minute, x.second)
print(q)