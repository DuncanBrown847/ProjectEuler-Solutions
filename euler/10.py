import math

result = 2
target = 2000000
prc = 1

for x in range(3, target, 2):
    
    if round(x/target * 100) == prc:
        print(str(prc) + "%")
        prc += 1
        
    prime = True

    '''for y in primelist:
        if x % y == 0:
            prime = False'''

    for y in range(2, math.ceil(math.sqrt(x)) + 1):
            if x % y == 0:
                prime = False
                break

    if prime:
        result += x

print(result)
