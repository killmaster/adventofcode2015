count = 0
world = set()

x = 0
y = 0
w = 0
z = 0

with open('day3input.txt') as f:
    for line in f:
        for character in line:
            if character == '>':
                if count % 2 == 0:
                    x += 1
                else:
                    w += 1
            elif character == '<':
                if count % 2 == 0:
                    x -= 1
                else:
                    w -= 1
            elif character == '^':
                if count % 2 == 0:
                    y += 1
                else:
                    z += 1
            elif character == 'v':
                if count % 2 == 0:
                    y -= 1
                else:
                    z -= 1
            world.add((x,y))
            world.add((w,z))
            count += 1

print("Result: "+ str(len(world)))
