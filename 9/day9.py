import re
from itertools import permutations

p1 = re.compile(r'(?P<origin>\w+) to (?P<destination>\w+) = (?P<distance>\d+)')

string = open('input.txt').read()
if string[-1] == '\n':
    string = string[:-1]
lines = string.split('\n')

parsed = {}
towns = []

for line in lines:
    origin = p1.match(line).group('origin')
    destination = p1.match(line).group('destination')
    distance = int(p1.match(line).group('distance'))
    parsed[(origin,destination)] = distance
    parsed[(destination,origin)] = distance

    if origin not in towns:
        towns.append(origin)
    if destination not in towns:
        towns.append(destination)

current_distance = 0
current_town = ""
shortest = 999999999999
longest = 0
permuted = list(permutations(towns))
limit = len(towns) - 1
for perm in permuted:
    for i in range(limit):
        current_distance += parsed[(perm[i],perm[i+1])]
    if current_distance < shortest:
        shortest = current_distance
    if current_distance > longest:
        longest = current_distance
    current_distance=0
print "result part1: ",shortest
print "result part2: ",longest
