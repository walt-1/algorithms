# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

def srtStr(stack, needle):
    if needle == "": return 0
    # range -> (includes, upto but not visit)
    # to protect from over indexing, range is set to stack len - needle len + 1 - plus one needed bc range stops one before int
    for i in range(0, len(stack) - len(needle) + 1):
        if stack[i : i + len(needle)] == needle:
            return i
    return -1

# SYS OUT
print(srtStr('hello', 'll'))