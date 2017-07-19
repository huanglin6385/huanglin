#86.48
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return None

        self.level = 0
        self.result = root.val
        def dfs(root,level):
            if root == None:
                return
            if level>self.level:
                self.result = root.val
                self.level = level

            dfs(root.left,level+1)
            dfs(root.right,level+1)

        dfs(root.left,1)
        dfs(root.right,1)
        return self.result