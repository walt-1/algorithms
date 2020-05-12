# Given an integer, write a function to determine if it is a power of three.
# Example 1:
# Input: 27
# Output: true

# Example 2:
# Input: 0
# Output: false

def is_power(n, p):
    if n == 0: return False
    while (n % p) == 0:
        n /= p
    return n == 1

print(is_power(81, 3))
