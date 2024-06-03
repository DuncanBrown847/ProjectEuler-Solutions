def genarray(dim):
    array = []
    
    for x in range(dim):
        array.append([])
        for y in range(dim):
            array[x].append(0)

    return array


def snake(grid, pos):
    #print(pos)
    if (pos[0] + 1 >= len(grid) and pos[1] + 1 >= len(grid[0])):
        return 1
    
    if pos[0] + 1 >= len(grid):
        return snake(grid, (pos[0], pos[1] + 1))
    elif pos[1] + 1 >= len(grid[0]):
        return snake(grid, (pos[0] + 1, pos[1]))
    else:
        return snake(grid, (pos[0], pos[1] + 1)) + snake(grid, (pos[0] + 1, pos[1]))


#assumes length = width
def snake2(gridlen, pos):
    #print(pos)
    if (pos[0] == gridlen - 1 or pos[1] == gridlen - 1):
        return 1
    elif pos[0] == pos[1]:
        return 2 * (snake2(gridlen, (pos[0], pos[1] + 1)))
    else:
        return snake2(gridlen, (pos[0], pos[1] + 1)) + snake2(gridlen, (pos[0] + 1, pos[1]))


#for x in range(1, 21):
x = 20
#print("snake1: " + str(x) + "x" + str(x) + ": " + str(snake(genarray(x + 1), (0,0))))
print("snake2: " + str(x) + "x" + str(x) + ": " + str(snake2(x + 1, (0,0))))
