# Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]


def product(nums):
    result = [1] * len(nums)
    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]
    
    R = 1
    for j in range(len(nums) - 1, -1,- 1):
        result[j] = result[j] * R
        R *= nums[j]

    return result

