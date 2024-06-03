largest = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        num = str(x * y)
        if num[:len(num)//2] == num[len(num)//2:len(num)][::-1]:
            print(str(x) + "*" + str(y) + " = " + num)

            if x * y > int(largest):
                largest = num
print(largest)
