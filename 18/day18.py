size = 100
original_board = [[0 for x in range(size)] for y in range(size)]

with open("input.txt") as f:
    i = 0
    for line in f:
        j = 0
        for char in line:
            if char == '#':
                original_board[i][j] = 1
            j += 1
        i += 1

def neighbors(board, x, y):
    res = 0
    if x > 0 and y > 0 and board[x-1][y-1] == 1:
        res += 1
    if x > 0 and board[x-1][y] == 1:
        res += 1
    if y > 0 and board[x][y-1] == 1:
        res += 1
    if x < size-1 and y < size-1 and board[x+1][y+1]:
        res += 1
    if x < size-1 and board[x+1][y]:
        res += 1
    if y < size-1 and board[x][y+1]:
        res += 1
    if x < 99 and y > 0 and board[x+1][y-1]:
        res += 1
    if x > 0 and y < 99 and board[x-1][y+1]:
        res += 1
    return res

def apply_iteration(board):
    new_board = [[0 for x in range(size)] for y in range(size)]
    for row in range(size):
        for col in range(size):
            adjacents = neighbors(board,row,col)
            if board[row][col] == 1 and adjacents == 2 or adjacents == 3:
                new_board[row][col] = 1
            elif board[row][col] == 0 and adjacents == 3:
                new_board[row][col] = 1
    return new_board

def apply_iteration_part2(board):
    new_board = [[0 for x in range(size)] for y in range(size)]
    new_board[0][0] = 1
    new_board[0][99] = 1
    new_board[99][0] = 1
    new_board[99][99] = 1
    for row in range(size):
        for col in range(size):
            if (row,col) in [(0,0),(0,99),(99,0),(99,99)]:
                continue
            adjacents = neighbors(board,row,col)
            if board[row][col] == 1 and adjacents == 2 or adjacents == 3:
                new_board[row][col] = 1
            elif board[row][col] == 0 and adjacents == 3:
                new_board[row][col] = 1
    return new_board

number_of_iterations = 100
board = original_board
for _ in xrange(number_of_iterations):
    board = apply_iteration(board)

def count_alive(board):
    res = 0
    for x in range(size):
        for y in range(size):
            if board[x][y] == 1:
                res += 1
    return res
print "part1: ",count_alive(board)
board[0][0] = 1
board[0][99] = 1
board[99][0] = 1
board[99][99] = 1
board = original_board
for _ in xrange(number_of_iterations):
    board = apply_iteration_part2(board)
print "part2: ",count_alive(board)
