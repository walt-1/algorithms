

def is_happy(n):
    '''
    input: int
    rtype: boolean
    '''
    # unique set of ints - holds sums to check for loops indicating not a happy num
    seen = set()
    # loop while n is not 1
    while n != 1:
        # holds n in a curnum var
        cur_num = n
        # init sqr sum to zero
        sqr_sum = 0
        # loop over each digit in cur num
        while cur_num != 0:
            # add square of cur digit -1s place- to sum
            sqr_sum += (cur_num % 10) * (cur_num % 10)
            # divides and sets cur num to that result - moving number over an order of mag
            cur_num /= 10
        
        # checks if current sum has been seen - returns false
        if sqr_sum in seen:
            return False
        # adds sum to seen
        seen.add(sqr_sum)
        # sets n to the calc sum of squared nums
        n = sqr_sum
    
    # if the loop runs to meet condition - return True
    return True


# SYS OUT
print(is_happy(4))
