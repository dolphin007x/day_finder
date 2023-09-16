def findDay(day, month, year):
    # arrange the days as per indices
    dayIndex = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

    # define k & j
    k = year % 100
    j = year // 100

    if month < 3:
        month += 12
        year -= 1

    h = (day + (13*(month+1) // 5) + k + (k // 4) + (j // 4) - 2*j) % 7

    d = ((h+5) % 7) + 1

    # makeshift debugger
   # print(f"d = {d} and the day is apparently {dayIndex[d]}")

    print(f"The day corresponding to {day}/{month}/{year} is {dayIndex[d-1]}")


x = input("Enter the day (DD) : ")
x = int(x)
y = input("Enter the month (MM) : ")
y = int(y)
z = input("Enter the year (YY) : ")
z = int(z)

findDay(x, y, z)
