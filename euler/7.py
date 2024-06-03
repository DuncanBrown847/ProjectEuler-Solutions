count = 1
num = 3

while count < 10001:
    prime = True

    for x in range(2, num):
        if num % x == 0:
            prime = False
            break
    if prime:
        count += 1
        print(count, num)

    num += 2
