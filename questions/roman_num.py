# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. 
# The number twenty seven is written as XXVII, which is XX + V + II.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:
# Input: "III"
# Output: 3

# Example 2:
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


def roman_num(s):
    rn = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # sets index to last char in string
    index = len(s) - 1
    # initializes count to last char value from hash map
    count = rn[s[index]]
    # decrements index after accounting for last char value to value needed for loop to start calculations
    index -= 1

    while index >= 0:
        # get cur char and map to its in value 
        cur_val = rn[s[index]]
        last_val = rn[s[index + 1]]
        
        # asserts current value in string is greater than the following value in the sequence
        if cur_val >= last_val: count += cur_val
        else: count -= cur_val

        index -= 1

    return count

# SYS OUT
print(roman_num("XLII"))
