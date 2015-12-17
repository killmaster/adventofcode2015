import itertools
total = 150
capacity = []
with open('input.txt') as f:
    for line in f:
        capacity.append(int(line))

def solver(data,total,part2=False):
    result = 0
    flag = False
    for i in range(len(data)):
        temp = 0
        for combination in itertools.combinations(data,i):
            if sum(combination) == total:
                temp += 1
                flag = True
        result += temp
        if part2 and flag:
            return temp
            break
    return result
print solver(capacity,total)
print solver(capacity,total,True)
