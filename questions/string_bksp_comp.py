# "#" means a backspace character.
# Given two strings S and T, return if they are equal when both are typed into empty text editors.

# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

def backspace_compare(S, T):

    s = list()
    for c in S:
        if c != "#":
            s.append(c)
        elif len(s) > 0:
            s.pop()
    
    t = list()
    for c in T:
        if c != "#":
            t.append(c)
        elif len(t) > 0:
            t.pop()

    while s:
        cur = s.pop()
        if not t or cur != t.pop():
            return False
    
    return not s and not t


# SYS OUT
print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("ab#c", "ad#c"))
