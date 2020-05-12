# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

# Example 1:
# Input: 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

def ham_weight(n):
    '''
    input: int
    rtype: int
    '''
    # init counter to 0
    c = 0
    while n:
        # The & operator evaluates if both digits in the current place are one - if so keeps 1 if either is zero - evals to zero: thus
        # 11 & 10 -> 00000000000000000000000000001011 & 00000000000000000000000000001010 -> n = 10 c = 1
        # 10 &= 9 -> 00000000000000000000000000001010 & 00000000000000000000000000001001 -> n = 8 c = 2
        # 8 &= 7 ->  00000000000000000000000000001000 & 00000000000000000000000000000111 -> n = 0 c = 3
        print(bin(n))
        n &= n - 1
        c += 1
    
    return c


# SYS OUT
w = ham_weight(11)
print("WEIGHT: " + str(w))
