# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses have security 
# system connected and it will automatically contact the police if two adjacent 
# houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each 
# house, determine the maximum amount of money you can rob tonight without
# alerting the police.

# Example 1:
# Input: [5, 2, 3, 5]
# Output: 4
# Explanation: Rob house 1 (money=1) and then rob house 3 (money=3)
# Total amount you can rob = 1 + 3 = 4

def rob(houses):
    # returns explicit values that do not require compute
    if len(houses) == 0 : return 0
    if len(houses) == 1 : return houses[0]
    if len(houses) == 2 : return max(houses[0], houses[1])

    # if there are more than two houses, calc is required
    # initializes a list of house length with None values to be set as calcs are made per house
    cache = [None] * len(houses)
    # sets initial known values 
    cache[0] = houses[0]
    cache[1] = houses[1]
    # loops from third house(idx2) to the last house
    for i in range(2, len(houses)):
        # finds max between current house value plus value two houses back or last house value
        # sets that max to current total value robbed from houses thus far
        cache[i] = max(houses[i] + cache[i - 2], cache[i - 1])
    # returns last value in the cached list (len minus 1 bc 0 idx) that holds aggregate of max values per house
    return cache[- 1]


# SYS OUT
print(rob([5, 2, 3, 5, 1, 3, 4]))