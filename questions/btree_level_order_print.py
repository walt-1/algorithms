# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree[3, 9, 20, null, null, 15, 7],
#     3
#    / \
#   9  20
#     /  \
#    15   7

# returns -> [[3],[9,20],[15,7]]

from TreeNode import TreeNode
def level_order_traversal(btree):

    # create a list for lists of level values for return
    tree_levels = list()
    # creates utility queue to process nodes on cur level
    queue = list()
    queue.append(btree)

    # continues bfs while nodes are in queue
    while queue:
        # list to hold values of nodes per level
        cur_level = list()
        # loop over nodes in current level
        for node in range(0, len(queue)):
            # deque list to get cur node and value
            cur_node = queue.pop(0)
            # appends value to cur level list
            cur_level.append(cur_node.val)
            # checks if cur node has children and enques the to next level to be processed
            if cur_node.left: queue.append(cur_node.left)
            if cur_node.right: queue.append(cur_node.right)
        
        # adds list of values for cur level to main list 
        tree_levels.append(cur_level)
    
    # return list of lists containing values of each level
    return tree_levels


btree = TreeNode(1, TreeNode(2, TreeNode(3, None, None),
                                 None), TreeNode(2, None, TreeNode(3, None, None)))

print("Level Order Traversal - BFS: " + str(level_order_traversal(btree)))
