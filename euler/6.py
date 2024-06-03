sosq = 0
sqos = 0

for x in range(1, 101):
    sosq += (x ** 2)
    sqos += x
sqos **= 2

print(sosq - sqos)
