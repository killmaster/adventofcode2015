WORLD_SIZE = 190

world = [[0 for x in range(WORLD_SIZE)] for x in range(WORLD_SIZE)]
x = WORLD_SIZE/2
y = WORLD_SIZE/2
w = WORLD_SIZE/2
z = WORLD_SIZE/2
count = 0
world[x][y] += 1
with open('day3input.txt') as f:
    for line in f:
        for character in line:
            if character == '>':
                if count % 2 == 0:
                    x += 1
                    world[x][y] += 1
                else:
                    w += 1
                    world[w][z] += 1
            elif character == '<':
                if count % 2 == 0:
                    x -= 1
                    world[x][y] += 1
                else:
                    w -= 1
                    world[w][z] += 1
            elif character == '^':
                if count % 2 == 0:
                    y += 1
                    world[x][y] += 1
                else:
                    z += 1
                    world[w][z] += 1
            elif character == 'v':
                if count % 2 == 0:
                    y -= 1
                    world[x][y] += 1
                else:
                    z -= 1
                    world[w][z] += 1

            count += 1

count = 0
empty = True
for i in range(WORLD_SIZE):
    line = str(i) + " |"
    for j in range(WORLD_SIZE):
        if world[i][j] > 0:
            count += 1
            empty = False
            line += "x"
        else:
            line += " "
    if not empty:
        print(line)
    empty = True
print("Result: "+ str(count))
