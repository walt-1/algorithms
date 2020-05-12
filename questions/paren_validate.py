# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 4:

# Input: "([)]"
# Output: false


def valid_parens(s):
    # create hash map 'str' open paren -> 'str' closed paren
    b = {
        '{':'}',
        '(':')',
        '[':']'
    }
    #  create a stack
    stack = list()
    # loop through char in paren string
    for p in s:
        # check open if so push it onto the stack
        if p in b:
            stack.append(p)
        # check if closing paren by checking hash map values
        if p in b.values():
        # check if char matches and pops next char off of stack
            if p == b[stack[-1]]:
                stack.pop()
            else:
                # else returns false
                return False

    # returns boolean: checks if stack is empty - if valid it should be
    return len(stack) == 0


# SYS OUT
print(valid_parens("([])"))
