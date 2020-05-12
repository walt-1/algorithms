# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
# The solution set must not contain duplicate triplets.
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

def three_sum(nums):
    # sort nums
    nums.sort()
    # create return list of ints
    result = set()
    numap = dict()

    # loop over nums in range - 2 to access 2 nums from anchor
    for i in range(len(nums)):
        numap[nums[i]] = i
    
    for i in range(len(nums) - 1):
        if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
            continue
        for j in range(i + 1, len(nums)):
            x,y = nums[i], nums[j]
            z = -(x + y)
            # skip duplicates
            if z < y:
                break
            if not (z in numap and numap[z] > j):
                continue
            s = (x,y,z)
            if s not in result:
                result.add(s)
                
    return result

# SYS OUT
print(three_sum([-1, 0, 1, 2, -1, -4]))
