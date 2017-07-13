#71.18
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """


        def dfs(root,target):
            if root == None:
                return False
            if root.val == target and root.left == None and root.right == None:
                return True

            return dfs(root.left,target-root.val) or dfs(root.right,target-root.val)


        return dfs(root,sum)