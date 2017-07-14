#72.84
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []

        def dfs(root, string):
            if root == None:
                return
            if root.left == None and root.right == None:
                result.append(string + "->" + str(root.val))
                return

            dfs(root.left, string + "->" + str(root.val))
            dfs(root.right, string + "->" + str(root.val))

        if root == None:
            return []

        if root.left == None and root.right == None:
            return [str(root.val)]
        dfs(root.left, str(root.val))
        dfs(root.right, str(root.val))
        return result