start = 20151125
target = (2978, 3083)
multiply = 252533
remainder = 33554393 

"""using a triangle to find the generation number of the code we want"""
def get_position(row, column):
    return sum(range(row + column - 1)) + column

def get_code(starting, row, column):
    stop = get_position(row, column)
    code = start
    for i in range(stop - 1):
        code = (code * multiply) % remainder
    return code

print get_code(start,target[0],target[1])
