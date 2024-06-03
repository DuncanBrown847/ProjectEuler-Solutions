import math

def divisors(n):
    tot
    for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0:
            print(str(x) + ', ' + str(n//x), end=' : ')

t = 0
for x in range(0, 10):
    t += x
    print(t)
    divisors(t)
    print('\n')