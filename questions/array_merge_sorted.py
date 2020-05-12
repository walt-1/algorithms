# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space(size that is greater or equal to m + n) to hold additional elements from nums2.

# Example
# Input:
# nums1 = [1, 2, 3, 0, 0, 0],  m = 3
# nums2 = [2, 5, 6],           n = 3

# Output: [1, 2, 2, 3, 5, 6]

# Answer :
# The key is to work backwards down both arrays using a pointer for each of their lengths
# Additionally, creating a third pointer with the sum of each array length (-1 for zero index) to set values within control statements


def merge_sorted_in_place(nums1, m, nums2, n):
    # create two pointers with length of two arrays - one for each array
    p1 = m - 1
    p2 = n - 1
    # create a merge index to set values in control statement
    mi = (m + n) - 1
    # loop while the index is greater than or equal to zero while decrementing merge index
    while p1 >= 0 and p2 >= 0:
        # check nums1 p1 is greater than nums p2
        if nums1[p1] > nums2[p2]:
            # set nums merge index to nums p1 and decrement p1
            nums1[mi] = nums1[p1]
            p1 -= 1
        else:
            # set nums merge index to nums p2 and decrement p2
            nums1[mi] = nums2[p2]
            p2 -= 1
        mi -= 1

    # loop while p2 is less than or equal to zero
    while p2 >= 0:    
        # set merge index to nums p2
        nums1[mi] = nums2[p2]
        # decrement p2
        p2 -= 1
        mi -= 1

    return nums1


nums1 = [1,2,3,4,5]
nums2 = [3,4,4,6,7]
print(merge_sorted_in_place(nums1, len(nums1), nums2, len(nums2)))
