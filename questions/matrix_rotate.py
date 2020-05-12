# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees(clockwise).
# Note:You have to rotate the image in-place, which means you have to modify the 
#  input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate(matrix):
    '''
    input type: int[][]
    rtype: int[][]
    '''
    if not matrix: return matrix
    # init var to length of matrix for math operations
    n = len(matrix)
    # loop over each item in matrix to perform swap across diag
    # 1 2 3     1 4 7
    # 4 5 6  -> 2 5 8  
    # 7 8 9     3 6 9
    for row in range(n):
        for col in range(row, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in range(n):
        for col in range(n//2):
            matrix[row][col], matrix[row][n-1-col] = matrix[row][n-1-col], matrix[row][col]

    return matrix

# SYS OUT
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for r in m: print(r)
print('-')

rotate(m)
for r in m: print(r)
