import calendar

yy = int(input("Year:"))
mm = int(input("month:"))
cal = calendar.month(yy, mm)
print(cal)