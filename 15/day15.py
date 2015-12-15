""" Rewritten version of /u/What-A-Baller solution"""
""" https://www.reddit.com/r/adventofcode/comments/3wwj84/day_15_solutions/cxzk44a """

import re

p1 = re.compile(r'(?P<name>\w+): capacity (?P<capacity>[-]?\d+), durability (?P<durability>[-]?\d+), flavor (?P<flavor>[-]?\d+), texture (?P<texture>[-]?\d+), calories (?P<calories>[-]?\d+)')
string = open('input.txt').read()
if string[-1] == '\n':
    string = string[:-1]
lines = string.split('\n')

ingredients  = []

for line in lines:
    name = p1.match(line).group('name')
    recapacity = int(p1.match(line).group('capacity'))
    redurability = int(p1.match(line).group('durability'))
    reflavor = int(p1.match(line).group('flavor'))
    retexture = int(p1.match(line).group('texture'))
    recalories = int(p1.match(line).group('calories'))
    ingredients .append([recapacity,redurability,reflavor,retexture,recalories])

""" Max bruteforce """
from itertools import combinations_with_replacement,permutations

def get_combinations(n,total):
    start = total if n == 1 else 0
    for i in range(start,total+1):
        if n-1:
            for j in get_combinations(n-1, total - i):
                yield [i] + j
        else:
            yield [i]

def calc(recipe, max_calories=0):
    proportions = [map(lambda x:x*mul, props) for props, mul in zip(ingredients, recipe)]
    dough = reduce(lambda a, b: map(sum, zip(a, b)), proportions)
    calories = dough.pop()
    result = reduce(lambda a, b: a*b, map(lambda x: max(x, 0), dough))
    if max_calories:
        if calories == max_calories:
            return result
        else:
            return 0
    else:
        return result

recipes = get_combinations(len(ingredients), 100)
print max(map(calc,recipes))
recipes = get_combinations(len(ingredients), 100)
print max(map(lambda r: calc(r, 500), recipes))
