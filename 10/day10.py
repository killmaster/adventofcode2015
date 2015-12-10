input = "1113222113"

def solver(input):
    result = ""
    current = input[0]
    count = 0
    for c in xrange(len(input)):
        if input[c] == current:
            count+=1
        else:
            result += str (count) + current
            current = input[c]
            count = 1
        if c == len(input)-1:
            result += str(count) + current
    return result

for i in range(0,40):
    input = solver(input)
print "Result part1: ",len(input)
for i in range (0,10):
    input = solver(input)
print "Result part2: ",len(input)
