import re

p1 = re.compile(r'(?P<name>\w+) can fly (?P<speed>\d+) km\/s for (?P<duration>\d+) seconds\, but then must rest for (?P<rest>\d+) seconds\.')
string = open('input.txt').read()
if string[-1] == '\n':
    string = string[:-1]
lines = string.split('\n')

raindeers = []
speed = {}
duration = {}
distance = {}
rest = {}
has_rested = {}
hop = {}
points = {}
time = 2503

for line in lines:
    name = p1.match(line).group('name')
    respeed = int(p1.match(line).group('speed'))
    reduration = int(p1.match(line).group('duration'))
    rerest = int(p1.match(line).group('rest'))
    raindeers.append(name)
    speed[name] = respeed
    duration[name] = reduration
    distance[name] = 0
    rest[name] = rerest
    has_rested[name] = 0
    hop[name] = 0
    points[name] = 0
for i in range(time):
    for raindeer in raindeers:
        if hop[raindeer] % duration[raindeer] == 0 and rest[raindeer] > has_rested[raindeer] and i != 0:
            has_rested[raindeer] += 1
        else:
            has_rested[raindeer] = 0
            distance[raindeer] += speed[raindeer]
            hop[raindeer] += 1
    current_max = distance[max(distance,key=distance.get)]
    for raindeer in raindeers:
        if distance[raindeer] == current_max:
            points[raindeer] += 1

print distance[max(distance,key=distance.get)]
print points[max(points,key=points.get)]
