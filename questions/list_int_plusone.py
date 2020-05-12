# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: [1, 2, 3]
# Output: [1, 2, 4]
# Explanation: The array represents the integer 123.

def plus_one(int_array):
    # initialize num to zero that will collect nums and perform addition
    int_builder = 0
    # loop over int array
    for n in range(len(int_array)):
        # set order/place of num using index
        order = len(int_array) - (n + 1)
        # use order to parse out next digit and concat to our num builder
        int_builder += int_array[n] * 10**order

    # increment the build int by one
    int_builder += 1
    # loop over int_builder converted to string, convert each num to type int
    result = [int(num) for num in str(int_builder)]
    # return array of integers
    return result

# SYS OUT
print(plus_one([1,2,3,4,6,7]))
