#67.67
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        self.min_depth = 0xFFFFFFF

        def dfs(root, depth):
            if root == None:
                return

            if root.left == None and root.right == None:
                self.min_depth = min(self.min_depth, depth + 1)
                return

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root.left, 1)
        dfs(root.right, 1)

        return self.min_depth
