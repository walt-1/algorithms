# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

def pascals_triangle(n):
    '''
    input: int
    rtype: array of arrays int -> int[][]
    '''
    # create triangle of 1s
    result = [[1] * i for i in range(1, n + 1)]
    # loop in range of input
    for r in range(1, n):
        # loop range between first and last index [1, ...loops... , 1]
        for i in range(1, len(result[r - 1])):
            # set calc num at matrix position
            result[r][i] = result[r - 1][i] + result[r - 1][i - 1]
    # return result 
    return result


# SYS OUT
print(pascals_triangle(7))