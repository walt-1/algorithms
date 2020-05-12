# Write a function to find the longest common prefix string amongst 
# an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower", "flow", "flight"]
# Output: "fl"

# Example 2:
# Input: ["dog", "racecar", "car"]
# Output: ""

def lng_prefix(strings):
    # initialize string to return
    prefix = ""
    # null check
    if not strings: return prefix
    # select any string to run comparisons of other strs against
    anchor_string = strings[0]
    # initialize index
    index = 0
    # loop through chars in anchor string
    for char in anchor_string:
        # loops through each string that is not the anchor string
        for i in range(1, len(strings)):
            # checks if index cur value is greater than 
            # len of current string
            if index >= len(strings[i]) or char != strings[i][index]:
                return prefix
        # set char to prefix
        prefix += char
        # increment index
        index += 1
    
    return prefix

# SYS OUT
print(lng_prefix(['flower', 'flow', 'florida']))