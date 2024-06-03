import math
import random

def shortest_path(dim):
    sums = [0,] * len(dim)

    for i in range(len(dim)):
        not_i_sum = 0
        for j in range(len(dim)):
            if j == i:
                continue
            not_i_sum += dim[j] 
        sums[i] = not_i_sum
    #sums[i] = sum of all dim[not i]'s
    
    min_difference = abs(sums[0] - dim[0])
    min_dif_i = 0
    
    for i in range(1, len(dim)):
        new_min_dif = abs(sums[i] - dim[i])
        if new_min_dif < min_difference:
            min_difference = new_min_dif
            min_dif_i = i
    
    return math.sqrt(sums[min_dif_i] * sums[min_dif_i] + dim[min_dif_i] * dim[min_dif_i])
   

def num_of_solutions(M):
    count = 0
    for i in range(1, M + 1):
        for j in range(i, M + 1):
            for k in range(j, M + 1):
                if shortest_path((i, j, k)) % 1 == 0:
                    count += 1
    return count

def zero(M, target, const = 128):
    if const == 0:
        return M

    print("calculating", M)
    c = num_of_solutions(M)
    print("\t::", c, '\n')
    
    if c < target:
        return zero(M + const, target, const)
        
    if c > target:
        const //= 2
        return zero(M - const, target, const)

#arbitrary starting M = 300
print(zero(300, 1000000))
