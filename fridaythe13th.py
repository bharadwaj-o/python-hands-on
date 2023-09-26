m=int(input("Enter the month (in MM format):"))
y=int(input("Enter the year (in YYYY format):"))
d=int(13)


def day_of_week(year, month, day):
	x = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	year -= month < 3
	return (year + int(year/4) - int(year/100) + int(year/400) + x[month-1] + day) % 7

weekday = day_of_week(y,m,d)
if weekday==5:
	print(True)
else:
	print(False)




