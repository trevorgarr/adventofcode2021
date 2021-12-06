"""
Advent of Code Day 3:

Trevor Garrood
"""
from collections import defaultdict

def part_one(lines):
    bit_count = defaultdict(int)
    for num in lines:
        num = list(num)
        for i in range(0, len(num)):
            if num[i] == "1":
                bit_count[i] += 1
    most_common_bits_str = ""
    for i in range(len(bit_count)):
        if int(bit_count[i]) >= (len(lines) - int(bit_count[i])):
            most_common_bits_str += "1"
        else:
            most_common_bits_str += "0"
    most_common_bits = int(most_common_bits_str, 2)
    least_common_bits_str = ""
    for i in range(0, len(most_common_bits_str)):
        if most_common_bits_str[i] == "1":
            least_common_bits_str += "0"
        else:
            least_common_bits_str += "1"
    least_common_bits = int(least_common_bits_str, 2)
    return most_common_bits, least_common_bits


def count_most_common_bit(binary_array, index):
    num_ones = 0
    for num in binary_array:
        if num[index] == "1":
            num_ones += 1
    return num_ones


def determine_max_bit_co2(binary_array, index):
    num_ones = count_most_common_bit(binary_array, index)
    return "0" if (num_ones >= (len(binary_array) - num_ones)) else "1"


def determine_max_bit_o2(binary_array, index):
    num_ones = count_most_common_bit(binary_array, index)
    return "1" if (num_ones >= (len(binary_array) - num_ones)) else "0"


def find_rating(binary_array, binary_num_len, is_o2):
    index = 0
    while len(binary_array) > 1:
        if index == binary_num_len:
            print("An error occured")
            break
        if is_o2:
            common_bit = determine_max_bit_o2(binary_array, index)
        else:
            common_bit = determine_max_bit_co2(binary_array, index)
        filtered_list = []
        for i in range(0, len(binary_array)):
            if binary_array[i][index] == common_bit:
                filtered_list.append(binary_array[i])
        index += 1
        binary_array = filtered_list
    binary_str = int("".join(binary_array[0]), 2)
    return binary_str


def part_two(lines):
    binary_array = []
    binary_num_len = len(lines[0])
    for num in lines:
        binary_array.append(list(num))
    o2 = find_rating(binary_array, binary_num_len, True)
    co2 = find_rating(binary_array, binary_num_len, False)
    print("Life support rating: " + str(o2 * co2))

if __name__ == "__main__":
    f = open("day3.txt", "r")
    data = f.read()
    lines = data.splitlines()
    gamma_one, epsilon_one = part_one(lines)
    answer_one = gamma_one * epsilon_one
    print("Subamarine power consumption: " + str(answer_one))
    part_two(lines)
    f.close()
