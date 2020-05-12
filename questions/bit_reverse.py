# Reverse bits of a given 32 bits unsigned integer.
# Example 1:
# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 4326


def rev(n):
    # format int to a bin string
    s = "{0:032b}".format(n)
    # reverse the string
    r = s[::-1]
    # convert back to integer base 2
    return int(r, 2)


# SYS OUT
print(rev(00000010100101000001111010011100))
