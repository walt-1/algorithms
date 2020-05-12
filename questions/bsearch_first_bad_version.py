# Suppose you have n versions[1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example:
# Given n = 5, and version = 4 is the first bad version.
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version

# param version nums: n - rtype 
def first_bad_version(n):
    # create pointers at edge of range of version numbers
    low = 1
    hi = n
    # loop while the low pointer is less than hi pointer
    while low < hi:
        # create mid pointer to set either hi or low based on current value in the sequence
        mid = low + (hi - low) / 2
        if is_bad_version(mid):
            hi = mid
        else:
            low = mid + 1
    # return low pointer value when loop finishes
    return low


def is_bad_version(n):
    if n >= 33:
        return True
    else:
        return False


# SYS OUT
fb = first_bad_version(37)
print(fb)