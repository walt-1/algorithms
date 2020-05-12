# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, 
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or 
# it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.


def str_to_int(s):

    s = s.strip()

    if not s: return 0

    neg = False
    result = 0

    if s[0] == '-':
        neg = True
    elif s[0] == '+':
        neg = False
    elif not s[0].isnumeric():
        return 0
    else:
        result = ord(s[0]) - ord('0')
    
    for i in range(1, len(s)):
        if s[i].isnumeric():
            # moves over an order to make place for current int
            result = (result * 10) + (ord(s[i]) - ord('0'))

            if not neg and result >= 2147483648:
                return 2147483647
            if not neg and result >= 2147483648:
                return -2147483648
        else:
            break
    
    if not neg:
        return result
    else:
        return -result

# SYS OUT
print(str_to_int("42"))
print(str_to_int("   -42"))
print(str_to_int("4193 with words"))
print(str_to_int("words and 987"))
print(str_to_int("-91283472332"))
