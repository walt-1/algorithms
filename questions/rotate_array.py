def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # resets k if num of places to rotate is greater than length of array
    k %= len(nums)
    length = len(nums)

    # reverse entire list in place
    # reverse k nums
    # re-reverse nums beyond k
    _reverse(nums, 0, length - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, length - 1)


def _reverse(nums, start, end):

    while(start < end):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
print(nums)
rotate(nums, 3)
print(nums)
