#83.2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.result = 0

        def dfs(root):
            l, r = 0, 0
            if root.left != None:
                l = dfs(root.left)
            if root.right != None:
                r = dfs(root.right)

            self.result += abs(l - r)
            return l + r + root.val

        dfs(root)
        return self.result