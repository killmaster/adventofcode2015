import re
from itertools import permutations

p1 = re.compile(r'(?P<person>\w+) would (?P<delta>\w+) (?P<happiness>\d+) happiness units by sitting next to (?P<other>\w+)\.')

string = open('input.txt').read()
if string[-1] == '\n':
    string = string[:-1]
lines = string.split('\n')

parsed = {}
people = []

for line in lines:
    person = p1.match(line).group('person')
    other = p1.match(line).group('other')
    happiness = int(p1.match(line).group('happiness'))
    delta = p1.match(line).group('delta')
    if delta == 'lose':
        happiness *= -1
    parsed[(person,other)] = happiness

    if person not in people:
        people.append(person)
    if other not in people:
        people.append(other)

permuted = list(permutations(people))
def get_results(permuted,people):
    limit = len(people)
    results = []
    current_happiness = 0
    for perm in permuted:
        for i in range(limit):
            person1 = perm[i]
            if i == 0:
                person2 = perm[limit-1]
            else:
                person2 = perm[i-1]
            if i == limit:
                person3 = perm[0]
            else:
                person3 = perm[(i+1) % limit]
            current_happiness += parsed[(person1,person2)]
            current_happiness += parsed[(person1,person3)]
        results.append(current_happiness)
        current_happiness=0
    return results

print "result part1: ",max(get_results(permuted,people))
for person in people:
    parsed[(person,'me')] = 0
    parsed[('me',person)] = 0
people.append('me')
print "result part2: ",max(get_results(list(permutations(people)),people))
