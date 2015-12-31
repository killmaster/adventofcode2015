import itertools
import operator
input_list = []

with open('input.txt') as f:
  for line in f:
    input_list.append(int(line.strip('\n')))

partitions = 3
limit = sum(input_list)/partitions

def solver(packages, parts):
  for i in range(1,len(packages)):
    for group in itertools.combinations(packages,i):
      if sum(group) == limit and parts == 2:
        return True
      elif sum(group) == limit and parts < partitions:
        return solver(list(set(packages) - set(group)), parts - 1)
      elif sum(group) == limit and solver(list(set(packages) - set(group)), parts - 1):
        return reduce(operator.mul, group, 1)
print 'part1:', solver(input_list, partitions)
partitions = 4
limit = sum(input_list)/partitions
print 'part2:', solver(input_list, partitions)
