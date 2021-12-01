"""
Advent of Code Day 1:
Submarine Depths
Trevor Garrood
"""


def part_one(nums):
    count_increases = 0
    for i in range(0, len(nums) - 1):
        if int(nums[i+1]) - int(nums[i]) > 0:
            count_increases += 1
    return count_increases


def part_two(nums):
    count_increases = 0
    window_sums = []
    for i in range(0, len(nums) - 2):
        window_sums.append(int(nums[i]) + int(nums[i+1]) + int(nums[i+2]))
    for j in range(0, len(window_sums) - 1):
        if window_sums[j+1] - window_sums[j] > 0:
            count_increases += 1
    return count_increases


if __name__ == "__main__":
    f = open("day1.txt", "r")
    data = f.read()
    nums = data.splitlines()
    num_sub_depth_increases_one = part_one(nums)
    print("The sub increased depth: " + str(num_sub_depth_increases_one) + " times at LOW accuracy")
    num_sub_depth_increases_two = part_two(nums)
    print("The sub increased depth: " + str(num_sub_depth_increases_two) + " times at HIGH accuracy")
    f.close()
