import math

notfound = True
count = round(math.sqrt(1020304050607080900))

while notfound:
    count += 1

    square = count ** 2
    print(square)
    
    comp = ''

    for x in range(0, len(str(square)), 2):
        comp += str(square)[x]
        
    if comp == '1234567890':
        notfound = False
        print("final", square)
    
