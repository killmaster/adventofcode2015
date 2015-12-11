import re

input = "vzbxkghb"
badcharacters = re.compile(r'[i|o|l]')
duplicated = re.compile(r'(.)\1')

def checkSequence(input):
    for i in xrange(len(input)-2):
        if ord(input[i]) == ord(input[i+1])-1 and ord(input[i]) == ord(input[i+2])-2:
            return True

def increaseChar(input):
    temp = list(input)[::-1]
    for i in xrange(len(temp)):
        if temp[i] == 'z':
            temp[i] = 'a'
        else:
            temp[i] = chr(ord(temp[i])+1)
            break
    return ''.join(temp[::-1])

def get_password(input):
    flag = False
    while not flag:
        input = increaseChar(input)
        if not checkSequence(input):
            #print input
            continue
        if badcharacters.search(input) is not None:
            #print "cenas2"
            continue
        if len(duplicated.findall(input)) < 2:
            #print "cenas3"
            continue
        flag = True
    return input

part1 = get_password(input)
print part1
part2 = get_password(part1)
print part2
