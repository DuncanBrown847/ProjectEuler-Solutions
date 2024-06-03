num = 0
notfound = True

while notfound:
    num += 20
    print(num)

    for x in [3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
        if num % x != 0:
            notfound = True
            break
        else:
            notfound = False
