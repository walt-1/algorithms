# The count-and-say sequence is the sequence of integers with the first 
# five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

def say_count(n):
    # initialize string to return to value of 1
    result = "1"
    # loop range 1 to len of int argument
    for i in range(1, len(n)):
        # mutates string until reach last num
        result = _say(result)

    return result

def _say(s):
    '''
    s: string
    rtype: string
    '''

    # inits vars to current char, count, and string builder 
    cur , count, say = s[0], 1, ''
    # range starts at 1 bc cur  is set
    for i in range(1, len(s)):
        # index i is a lookahead as the cur char being evaluated is set outside the loop
        nxt = s[i]
        # aggregates occurances of current char as it is appears in sequence
        if nxt == cur:
            count += 1
        else:
            # sets count of cur  with cur  to end of string builder
            say += (str(count) + cur )
            # sets cur  to last int accounted for and count back to 1
            cur , count = nxt, 1

    # at the end of the loop, count and cur  are set to nth int in count say seq
    say += (str(count) + cur )
    # return say
    return say
