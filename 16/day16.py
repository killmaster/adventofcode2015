import re
p1 = re.compile(r'Sue (?P<id>[-]?\d+): (?P<name1>\w+): (?P<quant1>[-]?\d+), (?P<name2>\w+): (?P<quant2>[-]?\d+), (?P<name3>\w+): (?P<quant3>[-]?\d+)')
string = open('input.txt').read()
if string[-1] == '\n':
    string = string[:-1]
lines = string.split('\n')

input_stuff = ['children','cats','samoyeds','pomeranians','akitas','vizslas','goldfish','trees','cars','perfumes']
input_quantities = [3,7,2,3,0,0,5,3,2,1]

input = zip(input_stuff,input_quantities)
current_max = 0
current_aunt = 0
aunts = {}

for line in lines:
    temp_aunt = int(p1.match(line).group('id'))
    n1 = p1.match(line).group('name1')
    q1 = int(p1.match(line).group('quant1'))
    n2 = p1.match(line).group('name2')
    q2 = int(p1.match(line).group('quant2'))
    n3 = p1.match(line).group('name3')
    q3 = int(p1.match(line).group('quant3'))
    aunts[temp_aunt] = {n1:q1,n2:q2,n3:q3}
    temp = set(input) & set([(n1,q1),(n2,q2),(n3,q3)])
    if temp > current_max:
        current_max = temp
        current_aunt = temp_aunt

print current_aunt

current_aunt = 0
for i, aunt in aunts.iteritems():
    res = dict(input)
    for k, v in dict(input).iteritems():
        if k not in aunt:
            del res[k]
        else:
            if k in ['cats','trees']:
                if aunt[k] > v:
                    del res[k]
            elif k in [ 'pomeranians','goldfish']:
                if aunt[k] < v:
                    del res[k]
            elif v == aunt[k]:
                del res[k]
    if len(res) < current_max:
        current_max = len(res)
        current_aunt = i

print current_aunt
