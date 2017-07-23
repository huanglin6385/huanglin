#77.61
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def dfs(root,level):
            if root == None:
                return
            if len(result) < level + 1:
                result.append(-0x80000000)

            result[level] = max(result[level],root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)

        if root== None:
            return []

        dfs(root,0)
        return result