# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

def is_pal(s):
    # validate string char and set each to and item in list
    st = [char for char in s.lower() if char.isalnum()] 
    # set pointers
    lo = 0
    hi = len(st) - 1
    # loop while pointers have not crossed
    while lo < hi:
        # assets chars at pointer are not equal
        if st[lo] != st[hi]:
            # returns false
            return False
        # increments lo
        lo += 1
        # decrements hi
        hi -= 1

    # if loop did not find unequal chars - returns true: valid palindrome
    return True

# SYS OUT
print(is_pal("A man, a plan, a canal: Panama"))
