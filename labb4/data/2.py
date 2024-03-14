import datetime

x = datetime.datetime.now()
a = int(x.day) - 1
b = int(x.day) + 1
print("Yesterday: " + str(x.year) + "-" + str(x.month) + "-" + str(a))
print("Today: " + str(x.year) + "-" + str(x.month) + "-" + str(x.day))
print("Tomorrow: " + str(x.year) + "-" + str(x.month) + "-" + str(b))