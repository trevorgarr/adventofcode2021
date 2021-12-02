"""
Advent of Code Day 2:
Submarine Depths with aim and horizontal position
Trevor Garrood
"""


def part_one(lines):
    horiz_pos = 0
    depth = 0
    for line in lines:
        command = line.split(" ")
        if command[0] == "forward":
            horiz_pos += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
    return depth, horiz_pos


def part_two(lines):
    horiz_pos = 0
    depth = 0
    aim = 0
    for line in lines:
        command = line.split(" ")
        if command[0] == "forward":
            horiz_pos += int(command[1])
            depth += (aim * int(command[1]))
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
    return depth, horiz_pos


if __name__ == "__main__":
    f = open("day2.txt", "r")
    data = f.read()
    lines = data.splitlines()
    depth_one, horiz_pos_one = part_one(lines)
    print("The sub changed depth by: " + str(depth_one) + " and horizontally travelled: " + str(horiz_pos_one))
    print("answer one: " + str(depth_one * horiz_pos_one))
    depth_two, horiz_pos_two = part_two(lines)
    print("The sub changed depth by: " + str(depth_two) + " and horizontally travelled: " + str(horiz_pos_two))
    print("answer two: " + str(depth_two * horiz_pos_two))
    f.close()
