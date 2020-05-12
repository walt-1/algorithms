
def btree_diam(root):

    diam = 1

    def _dfs(root):
        if root is None:
            return 0
        l = _dfs(root.left)
        r = _dfs(root.right)
        diam = max(diam, l + r + 1)
        return max(l, r) + 1
				
    _dfs(root)
    return diam - 1
