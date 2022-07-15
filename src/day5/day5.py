"""
Advent of Code Day 5
Vents
Trevor Garrood
"""


from os import X_OK


def part_one(input):
    # clean_data = clean_input(input)
    # print(clean_data)

    # find min and max
    # max_x, max_y = find_min_and_max(clean_data)
    # print(max_x, max_y)

    # initialize matrix of zeros that is min by max size
    # empty_matrix = initialize_matrix(max_x, max_y)
    # print(len(empty_matrix))
    [1, 0] -> [3, 2]
    clean_data = [[[0, 1], [3, 1]], [[1, 1], [1, 3]], [[0, 1], [0, 3]], [[1, 0], [1, 2]], [[3, 0], [3, 3]], [[0, 3], [3, 3]]]
    empty_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # iterate through input
    for val in clean_data:
        x1 = val[0][0]
        y1 = val[0][1]
        x2 = val[1][0]
        y2 = val[1][1]
        if x1 == x2 and y1 == y2:
            empty_matrix[x1][y1] += 1
        elif x1 == x2:
            draw_vertical(empty_matrix, y1, y2, x1)
        elif y1 == y2:
            draw_horizontal(empty_matrix, x1, x2, y1)
        elif (max(x1, x2) - min(x1, x2)) == (max(y1, y2) - min(y2, y1)):
            draw_diagonal(empty_matrix, x1, x2, y1, y2)
    sum = sum_dangerous(empty_matrix)
    print(sum)
    for row in empty_matrix:
        print(row)
    # if x1 == x2 draw vertical
    # if y1 == y2 draw horizontal
    # iterate through matrix and count all nums >= 2


def clean_input(nums):
    cleansed = []
    for line in nums:
        new_line = []
        line = line.split("->")
        interval_zero = line[0].strip().split(",")
        interval_one = line[1].strip().split(',')
        new_line.append(list(map(int, interval_zero)))
        new_line.append(list(map(int, interval_one)))
        cleansed.append(new_line)
    return cleansed


def find_min_and_max(clean_data):
    max_x = float("-inf")
    max_y = float("-inf")
    for line in clean_data:
        for pair in line:
            x = pair[0]
            y = pair[1]
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    return max_x, max_y


def initialize_matrix(max_x, max_y):
    return [[0 for _ in range(max_y)] for _ in range(max_x)]


def draw_horizontal(matrix, x1, x2, y):
    row = matrix[y]
    for i in range(min(x1, x2), max(x1, x2) + 1):
        row[i] += 1


def draw_vertical(matrix, y1, y2, x):
    for i in range(min(y1, y2), max(y1, y2) + 1):
        matrix[i][x] += 1


def sum_dangerous(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] >= 2:
                sum += 1
    return sum

def draw_diagonal(matrix, x1, x2, y1, y2):


def part_two(nums):
    pass


if __name__ == "__main__":
    f = open("day5.txt", "r")
    data = f.read()
    input = data.splitlines()
    part_one(input)
    f.close()
