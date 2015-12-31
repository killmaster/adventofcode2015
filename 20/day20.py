input = 33100000 
from collections import defaultdict
def part1(limit):
  houses = defaultdict(int)
  for elf in xrange(1,input):
    for house in xrange(elf,limit,elf):
      houses[house] += elf*10
    if houses[elf] >= input:
      return elf

def part2(limit):
  houses = defaultdict(int)
  elves = defaultdict(int)
  for elf in xrange(1,input):
    for house in xrange(elf,elf*50,elf):
      houses[house] += elf*11
    if houses[elf] >= input:
      return elf
print part1(1000000)
print part2(1000000)
