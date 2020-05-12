# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.
# Note:
# 0 ≤ x, y < 2**31

def ham_dist(x,y):
    # return bin(x ^ y).count('1')
    count = 0
    while x > 0 or y > 0:
        # increments count where the digit in the ones place is a "1" / all odd nums
        count += (x%2) ^ (y%2)
        # bit shifts x and y one to the right
        x >>= 1
        y >>= 1

    return count

# SYS OUT
print(ham_dist(1,4))
