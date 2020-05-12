# River Size 
# Graph traversal question
# Given a matrix thats doesnt have equal axis. 1s are rivers, 0s are land

# Ex.    [C]
# 1 0 0 1 0 [R]
# 1 0 1 0 0
# 0 0 1 0 1
# 1 0 1 0 1
# 1 0 1 1 0

# basic approach - brute force keeping track of where 1s are but this falls apart 
# bc the alg needs to know which river cur 1 belongs

# Time: O(n)
# Space: O(n)
def river_size(matrix):
    # initializes list to hold river lengths
    sizes = list()
    # initializes a matrix copy where values are all init to False 
    visited = [[False for col in row] for row in matrix]
    # loops over each item in matrix where item is type array 
    for row_i in range(len(matrix)):
        # loops through each item where item is 1 or 0
        for col_i in range(len(matrix[row_i])):
            # uses indecies of cur item in matrix to check value in matrix copy with boolean values
            if visited[row_i][col_i]:
                continue
            # moves to neighbor with reference indecies and curr
            traverse_vert(row_i, col_i, matrix, visited, sizes)
    return sizes

def traverse_vert(row_i, col_i, matrix, visited, sizes):
    cur_river_size = 0
    # applies depth first search iteratively
    # creates stack
    verts_to_explore = [[row_i, col_i]]

    while len(verts_to_explore):
        cur_vert = verts_to_explore.pop()
        row_i = cur_vert[0]
        col_i = cur_vert[1]
        if visited[row_i][col_i]:
            continue
        visited[row_i][col_i] = True
        if matrix[row_i][col_i] == 0:
            continue
        cur_river_size += 1
        # gets unvisited neighbors
        unvisited_neis = get_unvisited_neis(row_i, col_i, matrix, visited) # O(1)
        for neighbor in unvisited_neis:  # O(1)
            verts_to_explore.append(neighbor)

    if cur_river_size > 0:
        sizes.append(cur_river_size)


def get_unvisited_neis(row_i, col_i, matrix, visited):
    unvisited_neis = list()
    # checks that neighbors are valid and not visited
    # not visited the neighbor above
    if row_i > 0 and not visited[row_i - 1][col_i]:
        unvisited_neis.append([row_i - 1, col_i])
    # if not in the bottom row
    if row_i < len(matrix)-1 and not visited[row_i + 1][col_i]:
        unvisited_neis.append([row_i + 1, col_i])
    # not in left most column
    if col_i > 0 and not visited[row_i][col_i - 1]:
        unvisited_neis.append([row_i, col_i - 1])
    # dealing with row
    if col_i < len(matrix[0])-1 and not visited[row_i][col_i + 1]:
        unvisited_neis.append([row_i, col_i + 1])
    return unvisited_neis


matrix=[[1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]]

river_sizes = river_size(matrix)
print(river_sizes)
