def collatz(count, num):
    if num == 1:
        return count

    if num%2 == 0:
        return collatz(count + 1, num / 2)

    if num%2 == 1:
        return collatz(count + 1, (num * 3) + 1)


largest = 0
largest_col = 0

for x in range(1, 1000000, 2):
    current = collatz(1, x)
    print(x)
    if current > largest_col:
        largest = x
        largest_col = current

print(largest)
    
