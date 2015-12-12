## First part because it was quick
# import re
#
# numbers = re.compile(r'[-]?\d+')
#
# input = ""
#
# with open('input.txt') as myfile:
#   input = myfile.read()
#
# temp = numbers.findall(input)
# sum = 0
# for num in temp:
#     sum += int(num)
# print sum

# Second part because it works for the filtering
import json
input = json.loads(open('input.txt').read())
def get_numbers(input):
    #find the red in the json and not the array
    if type(input) == type(dict()):
        if 'red' in input.values():
            return  0
        return sum(map(get_numbers, input.values()))
    if type(input) == type(list()):
        return sum(map(get_numbers, input))
    if type(input) == type(0):
        return input
    return 0

#to print the first part too
import re
numbers = re.compile(r'[-]?\d+')
print sum(map(int,numbers.findall(open('input.txt').read())))
print get_numbers(input)
