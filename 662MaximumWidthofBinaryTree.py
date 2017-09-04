#70.3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        stack = []

        def dfs(height, node, value):
            if len(stack) <= height:
                stack.append([value, value])

            stack[height][0] = min(stack[height][0], value)
            stack[height][1] = max(stack[height][1], value)
            if node.left:
                dfs(height + 1, node.left, value << 1)

            if node.right:
                dfs(height + 1, node.right, (value << 1) + 1)

        if root != None:
            dfs(0, root, 0)
        else:
            return 0

        result = max(s[1] - s[0] + 1 for s in stack)
        return max(1, result)
