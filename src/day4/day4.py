"""
Advent of Code Day 4:
Bingo
Trevor Garrood
"""
from textwrap import wrap


def generate_boards(lines):
    board_collection = []
    single_board = []
    for line in lines:
        if line != "":
            single_board.append(wrap(line, 2))
        elif line == "":
            board_collection.append(single_board[:])
            single_board.clear()
    return board_collection


def mark_numbers(num, board):
    for line in board:
        for i in range(len(line)):
            if line[i] == num:
                line[i] = "x"


def sum_board(board):
    total = 0
    for line in board:
        for num in line:
            if num != "x":
                total += int(num)
    return total


def check_win(board):
    diagonal = 0
    for i in range(len(board)):
        valid_column = 0
        for row in board:
            if row == ["x", "x", "x", "x", "x"]:
                return True
            if row[i] == "x":
                valid_column += 1
        if board[i][i] == "x":
            diagonal += 1
        if valid_column == len(board):
            return True
    if diagonal == len(board):
        return True
    return False

def part_one():
    for number in random_input:
        for board in bingo_boards:
            mark_numbers(number, board)
            if check_win(board):
                return sum_board(board) * int(number)

def part_two(random_input, bingo_boards):
    called_num_idx = 0
    winning_boards = set()
    while len(winning_boards) < len(bingo_boards):
        called_num = random_input[called_num_idx]
        mark_numbers(called_num, bingo_boards)
        for i in range(len(bingo_boards)):
            is_game_over = check_win(bingo_boards[i])  # got fucked up with changes, dont have time to resolve
            print(is_game_over, i)
            if is_game_over:
                winning_boards.add(i)
        called_num_idx += 1
        print(len(winning_boards))
    board_sum = sum_board(bingo_boards[64])
    print(winning_boards)
    just_called = int(random_input[called_num_idx - 1])
    return board_sum * just_called


if __name__ == "__main__":
    f = open("day4.txt", "r")
    data = f.read()
    lines = data.splitlines()
    random_input = lines[0].split(",")
    bingo_boards = generate_boards(lines[2:])
    p1 = part_one()
    print("Part One:", p1)
    p2 = part_two(random_input, bingo_boards)
    print("Part Two:", p2)
    f.close()
