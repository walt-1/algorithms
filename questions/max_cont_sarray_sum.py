# Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.

def max_cont_subarray(nums):
    # We default to say the the best total_max seen so far is the first element.
    # We also default to say the the local_max ending at the first element is the first element
    total_max = nums[0];
    local_max = nums[0];
    # We will investigate the rest of the items in the array from index 1 onward
    for i in range(len(nums)):
        # Answering the question: "What is the Max Contiguous Subarray Sum we can achieve ending at index i?"
        # We have 2 choices:
        # local_max + nums[i] (extend the previous subarray best whatever it was)
        #   1.) Let the item we are sitting at contribute to this best max we achieved
        #   ending at index i - 1.
        # nums[i] (start and end at this index)
        #   2.) Just take the item we are sitting at's value.
        # The max of these 2 choices will be the best answer to the Max Contiguous Subarray Sum we can achieve for subarrays ending at index i.
        # indecies  0  1   2  3   4  5  6   7  8
        # Input: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
        #localmax  -2, 1, -2, 4,  3, 5, 6,  1, 5

        # The best subarrays we would take if we took them:
        #   ending at index 0: [ -2 ]
        #   ending at index 1: [ 1 ]
        #   ending at index 2: [ 1, -3 ]
        #   ending at index 3: [ 4 ]
        #   ending at index 4: [ 4, -1 ]
        #   ending at index 5: [ 4, -1, 2 ]
        #   ending at index 6: [ 4, -1, 2, 1 ]
        #   ending at index 7: [ 4, -1, 2, 1, -5 ]
        #   ending at index 8: [ 4, -1, 2, 1, -5, 4 ]
        # Notice how we are changing the end bound by 1 everytime
        local_max = max(local_max + nums[i], nums[i])
        # Did we beat the 'total_max' with the 'local_max'?
        total_max = max(total_max, local_max)

    return total_max

# SYS OUT

m = max_cont_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(m)