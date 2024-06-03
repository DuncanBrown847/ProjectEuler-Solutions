total = 0

with open("13.txt", "r") as F:
    for line in F.readlines():
        total += int(line.strip())

print(total)