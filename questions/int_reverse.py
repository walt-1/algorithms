# Given a 32-bit signed integer, reverse digits of an integer
# if questions are in a primitive type, the solution will likely act on the primitive type without conversion

def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    # n = num of digits
    # time: O(n)
    # space: O(1)

    result = 0
    remaining = abs(x)

    while remaining != 0:
        # preserves 1s place by creating 0 in the 1s place
        result *= 10  # 0 -> 0

        # extract ones place from remaining num and appends it to the end
        result += remaining % 10  # 123 -> 3; 0 -> 3

        # div by 10 to get rid of 1s place processing
        remaining /= 10  # 123 -> 12

    return result if result > 0 else -result
