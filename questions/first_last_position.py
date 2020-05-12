# Assumes sorted array
# Because binary search cuts the search space roughly in half on each iteration,
# there can be at most log10(n) iterations. Binary search is invoked twice, so the overall complexity is logarithmic.

# array<int>, int: rtype array<int>
def fst_lst_pos(nums, target):
    # binary search get left
    left_i = _bs_get_index(nums, target, True)
    # check if target exists in nums
    if left_i == len(nums) or nums[left_i] != target:
        return [-1, -1]
    # returns two indecies, second index is returned via bs
    return [left_i, _bs_get_index(nums, target, False)-1]

# array<int>, int, boolean: rtype int
def _bs_get_index(nums, target, left):
    lo = 0
    hi = len(nums)

    # loop while indecies are separted
    while lo < hi:
        # calc mid index
        mid = (hi + lo) // 2
        # asserts cur items in array is greater target or
        #   left and target equals cur item
        if nums[mid] > target or (left and nums[mid] == target):
            hi = mid
        else:
            lo = mid + 1

    return lo


a = [5, 7, 7, 8, 8, 10]
leng = fst_lst_pos(a, 8)
print(leng)
