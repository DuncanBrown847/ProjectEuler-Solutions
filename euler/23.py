def pfactors(n):
    S = [1]
    while n > 1:
        for i in range(2, n//2 + 2):
            if n % i == 0:
                n = n // i
                S += [i]
                break
        else:
            S += [n]
            n = 1
    return S

def divisors(n):
    S = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            S += [i]
    return S

def is_abundant(n):
    return sum(divisors(n)) > n

#for x in range(2, 28123):
#    print(f"{x}: {divisors(x)}")

X = []
for x in range(2, 28214):
    if (is_abundant(x)):
        X += [x] 

total = 0

for target in range(2, 28214):
    flag = False
    for i, A in enumerate(X):
        for B in X[i:]:
            if A+B == target:
                print(f"found: {target} ({A} + {B})")
                flag = True
                break
                
            elif A > target:
                flag = True
                print(f"\texhausted: {target}")
                total += target
                break
                
            elif A+B > target:
                break
                
        if flag:
            break
print(total)