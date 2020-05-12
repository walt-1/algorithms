# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:
# Given the sorted array: [-10, -3, 0, 5, 9],
# One possible answer is: [0, -3, 9, -10, null, 5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

from TreeNode import TreeNode

def sorted_array_bst(nums):
    # null check on array
    if not nums: return None
    # return helper function -> args: array, left index, right index
    return _construct_bst(nums, 0, len(nums) - 1)

# create helper function
def _construct_bst(nums, left, right):
    # BASE CASE
    # check if left index is greater than right index
    if left > right: return None

    # create midpoint using integer overflow 
    mid = left + (right - left) / 2
    # create a current node using nums value at mid index
    cur_node = TreeNode(nums[mid], None, None)
    # set left child using recursive statement
    cur_node.left = _construct_bst(nums, left, mid - 1)
    # set right child using recursive statement
    cur_node.right = _construct_bst(nums, mid + 1, right)
    # return current node
    return cur_node

def print_tree(tree):
    if not tree: return None
    
    cur_level = list()
    queue = list()
    queue.append(tree)

    while queue:
        for node in range(0, len(queue)):
            cur_node = queue.pop(0)
            cur_level.append(cur_node.val)
            if cur_node.left: queue.append(cur_node.left)
            if cur_node.right: queue.append(cur_node.right)    
    print(cur_level)
            

# SYS OUT        
sorted_list = [-10, -3, 0, 5, 9]
bal_tree = sorted_array_bst(sorted_list)
print_tree(bal_tree)
