largest = 0
num = 600851475
prc = 1

for x in range(3, num + 1):
    if round(x/num * 100) == prc:
        print(str(prc) + "%")
        prc += 1
        
    if num % x == 0:
        prime = True
        for y in range(2, x):
            if x % y == 0:
                prime = False
                break
        if prime:
            print(x, "prime factor")
            largest = x
print(largest, "largest prime factor")
