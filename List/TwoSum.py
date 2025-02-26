from math import remainder

nums = [2,7,11,15]
t = 9

def two_sum(nums, target):
    num_map = {}  # Dictionary to store numbers and their indices
    for i, num in enumerate(nums):
        complement = target - num  # Find the required pair
        if complement in num_map:
            return [num_map[complement], i]  # Return indices of the pair
        num_map[num] = i  # Store index of the current number
    return []



print(two_sum(nums, t))