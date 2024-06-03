import random as r
import sys

def trial():
    ls = []
    ls.append(r.randint(0, 999))

def experiment(n):
    count = 0
    
    for i in range(n):
        if trial():
            count += 1
    
    return count/n

def fn(n):
    #probability of a win in 'n' 
    #see https://www.desmos.com/calculator/d4nsvguaza
    
    result = 1.0
    
    for i in range(1, n):
        result *= (1 - ((1 - 0.001) * (1 - ((1 - 0.001) ** i))))
        print(i, "::", result)
    
    return 1 - result

if __name__ == "__main__":
    print(fn(2))
    print(fn(3))
    print(fn(5))
    print(fn(10))
