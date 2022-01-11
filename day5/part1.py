filter_strings = ['-> ', '\n']
line_cords = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.replace(' -> ', ',')
        line = line.replace('\n', '')
        line = line.split(',')
        for i in range(len(line)):
            line[i] = int(line[i])
        line_cords.append(line)


'''
Currently the list is filled with line cords lists. For each list
the indexs are
[0] = starting X
[1] = starting Y
[2] = end X
[3] = end Y
The starting pos isn't always smaller than the ending pos. So going to need to detect that'''


def get_max_pos(cords):
    all_x = []
    all_y = []
    for line in cords:
        all_x.append(line[0])
        all_x.append(line[2])
        all_y.append(line[1])
        all_y.append(line[3])
    max_x = max(all_x)
    max_y = max(all_y)
    return max_x, max_y


def get_blank_board(x_lim, y_lim):
    board = [[] for x in range(x_lim)]
    for x in range(x_lim):
        for y in range(y_lim):
            board[x].append("-")
    return board


def print_board(board):
    for x in range(len(board[i])):
        print("|" + str(x).rjust(3), sep='', end='')
    print("|")
    for x in range(len(board)):
        print('|', sep='', end='')
        for y in range(len(board)):
            print(board[x][y].rjust(4), sep='', end='')
        print('   |')


max_x, max_y = get_max_pos(line_cords)
main_board = get_blank_board(max_x, max_y)
print_board(main_board)
