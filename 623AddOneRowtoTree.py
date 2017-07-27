#42.16
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """

        def dfs(root, depth, sign=False):
            if depth == d:
                p = TreeNode(v)
                if sign:
                    p.left = root
                    return p
                else:
                    p.right = root
                    return p
            if root == None:
                return
            if depth < d - 1:
                dfs(root.left, depth + 1)
                dfs(root.right, depth + 1)
            elif depth == d - 1:
                root.left = dfs(root.left, depth + 1, True)
                root.right = dfs(root.right, depth + 1)

        if d == 1:
            p = TreeNode(v)
            p.left = root
            return p
        dfs(root, 1)
        return root