from random import shuffle

inputs = []

with open("input.txt") as file:
  for line in file:
    inputs.append(set(line.rstrip().split('=> ')))

reps = inputs[:-2]
mol = inputs[-1]

target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print part2
