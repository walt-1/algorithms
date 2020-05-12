# Determine if a 9x9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

def s_validate(board):
    # create a hash set to store visited cells: {string: boolean}
    seen = dict()

    # loops over rows and cols
    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            # set value at cur cell
            cur_val = board[r][c]
            if cur_val != ".":
                # creates string representations of cur cell
                row, col , box = cur_val + " in row " + str(r), cur_val + " in col " + str(c), cur_val + " in box " + str(r//3) + str(c//3)
                # checks if any aspect of cur cell state contains cur val
                if row in seen or col in seen or box in seen:
                    return False
                # sets string reps to key in hash set
                seen[row] = seen[col] = seen[box] = True
    
    # returns true if all cells contain valid values
    return True

# SYS OUT
b = [
    ["6", "3", ".", ".", "7", ".", ".", ".", "."], 
    ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
    [".", "9", "8", ".", ".", ".", ".", "6", "."], 
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
    [".", "6", ".", ".", ".", ".", "2", "8", "."], 
    [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
print(s_validate(b))
