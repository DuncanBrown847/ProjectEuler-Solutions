found = False
result = None

for x in range(1, 998):
    for y in range(1, 999 - x):
        z = 1000 - x - y

        if (x**2 + y**2 == z**2):
            print(x, y, z, x*y*z)
            found = True
            break
        
    if found:
        break
