#65.2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        result = 0
        stack = [root]
        while stack:
            head = stack.pop(0)
            if head.left:
                stack.append(head.left)
                if head.left.left == None and head.left.right == None:
                    result += head.left.val
            if head.right:
                stack.append(head.right)

        return result