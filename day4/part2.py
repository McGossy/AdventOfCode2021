# this project is a mock-up bingo. Made up of pre-determined numbers to be drawn
# and pre-determined boards that are in play
# goal is to draw the numbers one at a time, mark the boards with that number
# and find the last board to win
# win condition only checks for 5 in a row, or 5 in a column. No diagonal checks.
import re
number_pattern = re.compile(r"\d+")
lines = ""
with open('input.txt', 'r') as file:
    lines = file.readlines()

# gather the numbers to be drawn
draw_pile = []
matches = number_pattern.finditer(lines[0])
for match in matches:
    draw_pile.append(match.group())
del lines[0]
print(draw_pile)

# Gather every board. Put into 2D list. Boards are represented as a 1D list
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
# drop the first element since its a blank list and idk how else to fix that lol
boards = boards[1::]
print("\n|new gen boards|")
for board in boards:
    print(board)
print("\n|full new boards|\n", boards)

# print a list of boards
def print_boards(boards):
    for i in range(len(boards)):
        print("\n")
        for j in range(len(boards[i])):
            if j % 5 == 0:
                print()
            print(boards[i][j], end=' ')

# print one board
def print_board(board):
    for i in range(len(board)):
        if i % 5 == 0:
            print()
        print('|' + board[i].rjust(3), end=' ')
    print("\n")

# checking win conditions
def check_win(board):
    for i in range(0, len(board), 5):
        win_count = 0
        for j in range(i + 1, i + 5):
            if '*' in board[i] and '*' in board[j]:
                win_count += 1
            if win_count == 4:
                return True
    for i in range(5):
        win_count = 0
        for j in range(i + 5, len(board), 5):
            if '*' in board[i] and '*' in board[j]:
                win_count += 1
            if win_count == 4:
                return True

# draw next number and update all boards if the board has the number drawn
def draw_and_update_boards(i, draw_pile, boards):
    for j in range(len(boards)):
        for k in range(len(boards[j])):
            if str(draw_pile[i]) == boards[j][k]:
                boards[j][k] = "*" + boards[j][k]
    return boards

# not used. But will remove all the marks on the board
def remove_marks(board):
    for i in range(len(board)):
        if '*' in board[i]:
            board[i] = board[i][1:]
    return board

# ignores the numbers that were picked. Sums up the remaining numbers
def get_sum_board(board):
    sum = 0
    for i in range(len(board)):
        if '*' not in board[i]:
            sum += int(board[i])
    return sum


# main game loop
def play_game():
    last_board_to_win = []
    winning_board = []
    winning_board_indexes = []
    winning_num = 0
    for i in range(len(draw_pile)):
        draw_and_update_boards(i, draw_pile, boards)
        for j in range(len(boards)):
            if check_win(boards[j]):
                print(f"board[{j}] wins!")
                winning_board_indexes.append(j)
                winning_num = int(draw_pile[i])
        if len(winning_board_indexes) >= 1:
            print("\nWinning board indexes: ", winning_board_indexes)
            print("Last index: ", winning_board_indexes[-1])
            last_board_to_win = boards[winning_board_indexes[-1]]
            print("winning number: ", winning_num)
            print("last board to win: ")
            print_board(last_board_to_win)
        for i in range(len(winning_board_indexes)):
            idx = winning_board_indexes[i]
            del boards[idx - i]
        winning_board_indexes = []

    print('\n\n|LAST WINNING BOARD|')
    print_board(last_board_to_win)

    winning_sum = get_sum_board(last_board_to_win)
    print("sum of board: ", winning_sum)
    print("winning num: ", winning_num)
    print("final score = ", winning_sum * winning_num)


play_game()
