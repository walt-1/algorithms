# Given a binary tree, check whether it is a mirror of itself(ie, symmetric around its center).

# For example, this binary tree[1, 2, 2, 3, null, null, 3] is symmetric:
#     1
#    / \
#   2   2
#  /     \
# 3       3

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

def is_symmetric(btree):
    return _mirror_recurse(btree, btree)

def _mirror_recurse(n1, n2):    
    # Base Case
    # asserts both nodes are null
    if not n1 and not n2: return True
    # asserts only one of the nodes are null
    if not n1 or not n2: return False

    # Subroutine
    # asserts values are the same 
    # recurses using node one left and node two right 
    # recurses using node two left and node one right 
    return (n1.val and n2.val) and _mirror_recurse(n1.left, n2.right) and _mirror_recurse(n2.left, n1.right)


# SYS OUT
from TreeNode import TreeNode
sym_btree = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(2, None, TreeNode(3, None, None)))
non_sym_btree = TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)), TreeNode(2, None, TreeNode(3, None, None)))
print("Symmetric Tree returns: " + str(is_symmetric(sym_btree)))
print("Non Symmetric Tree returns: " + str(is_symmetric(non_sym_btree)))
