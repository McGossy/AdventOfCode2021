import re
number_pattern = re.compile(r"\d+")
lines = ""
with open('input.txt', 'r') as file:
    lines = file.readlines()

draw_pile = []
matches = number_pattern.finditer(lines[0])
for match in matches:
    draw_pile.append(match.group())
del lines[0]
print(draw_pile)

'''
board_num = -1
num = ''
boards = [[] for i in range(3)]
# getting all the numbers for the boards
for i in range(len(lines)):
    matches = number_pattern.finditer(lines[i])
    for match in matches:
        boards[board_num].append(match.group())
    if lines[i] == '\n':
        board_num += 1
print("\n|First gen boards|")
for board in boards:
    print(board)
'''

board_num = -1
boards = []
b = []
for i in range(len(lines)):
    matches = number_pattern.finditer(lines[i])
    for match in matches:
        b.append(match.group())
    if lines[i] == '\n':
        if len(b) < 0:
            board_num += 1
        else:
            boards.append([])
            for nums in b:
                boards[board_num].append(nums)
            b = []
boards = boards[1::]
print("\n|new gen boards|")
for board in boards:
    print(board)
print("\n|full new boards|\n", boards)


def print_boards(boards):
    for i in range(len(boards)):
        print("\n")
        for j in range(len(boards[i])):
            if j % 5 == 0:
                print()
            print(boards[i][j], end=' ')


def print_board(board):
    for i in range(len(board)):
        if i % 5 == 0:
            print()
        print(board[i], end=' ')
    print()


print("\n\nboards")
print_boards(boards)


def check_win(board):
    print("\nTrying row check")
    for i in range(0, len(board), 5):
        win_count = 0
        for j in range(i + 1, i + 5):
            if '*' in board[i] and '*' in board[j]:
                win_count += 1
                print(board[i], "marked, ", board[j], "marked")
            if win_count == 4:
                return True
    print("\nTrying column check")
    for i in range(5):
        win_count = 0
        for j in range(i + 5, len(board), 5):
            if '*' in board[i] and '*' in board[j]:
                win_count += 1
                print(board[i], "marked, ", board[j], "marked")
            if win_count == 4:
                return True


def draw_and_update_boards(i, draw_pile, boards):
    for j in range(len(boards)):
        for k in range(len(boards[j])):
            if str(draw_pile[i]) == boards[j][k]:
                boards[j][k] = "*" + boards[j][k]
    return boards


winning_board = []
winning_num = 0
for i in range(len(draw_pile)):
    draw_and_update_boards(i, draw_pile, boards)
    if winning_num > 0:
        break
    for j in range(len(boards)):
        if check_win(boards[j]):
            print(f"board[{j}] wins!")
            winning_board = boards[j]
            winning_num = int(draw_pile[i])

print('\n\n|WINNING BOARD|')
print_board(winning_board)


def remove_marks(board):
    for i in range(len(board)):
        if '*' in board[i]:
            board[i] = board[i][1:]
    return board


def get_sum_board(board):
    sum = 0
    for i in range(len(board)):
        if '*' not in board[i]:
            sum += int(board[i])
    return sum



winning_sum = get_sum_board(winning_board)
print(winning_sum)
print(winning_num)
print("final score = ", winning_sum * winning_num)


def check_win_all(boards):
    winning_boards = []
    for board in boards:
        for i in range(0, len(board), 5):
            win_count = 0
            for j in range(i + 1, i + 5):
                if '*' in board[i] and '*' in board[j]:
                    win_count += 1
                if win_count == 4:
                    winning_boards.append(board)
        for i in range(5):
            win_count = 0
            for j in range(i + 5, len(board), 5):
                if '*' in board[i] and '*' in board[j]:
                    win_count += 1
                if win_count == 4:
                    winning_boards.append(board)
    return winning_boards

print("\n\nAll winning boards?")
print_boards(boards)
