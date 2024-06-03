ls = [1, 2]
result = 0

while ls[1] <= 4000000:
    ls.append(sum(ls))
    del ls[0]
    if ls[0] % 2 == 0:
        result += ls[0]

print(result)
