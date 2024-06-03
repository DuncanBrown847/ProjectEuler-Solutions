c = 0
total = -2 #adjustment to ignore first 2 sundays from 1900

for year in range(1900, 2001):
    for month in range(12):
        if c == 6:
            total += 1
            #print(f"{year} {month}")
    
        days = 0
        if month in [3, 5, 8, 10]:
            days = 30
        elif month == 1:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                days = 29
            else:
                days = 28
        else:
            days = 31

        c = (c + days) % 7

print(total)

#passed test on 2/22/2024 5:04 AM!