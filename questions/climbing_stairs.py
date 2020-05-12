# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer
# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

def climb_stairs(n):
    # use memoization to utilize storage to access solved subproblems
    if n == 1: return 1
    first = 1
    second = 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second


# def climb_stairs_fib(n):
#     sqrt5 = math.sqrt(5)
#     fibn = ((1+sqrt5)/2)**(n+1) - ((1-sqrt5)/2)**(n+1)
#     return int(fibn/sqrt5)
