# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
# Note:
#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.


def move_zeros(array):
    # create pointer one to keep track of zeros
    p = 0
    # loops over each num in array
    for i in range(len(array)):
        print(p, i)
        # checks if num is not zero
        if array[i] != 0:
            # swap current num -in place- to the left without disrupting order
            array[i], array[p] = array[p], array[i]
            # increments pointer
            p += 1
    # return mutated array
    return array

# SYS OUT
print(move_zeros([0,2,0,32,4,8,9]))