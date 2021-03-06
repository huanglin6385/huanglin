#78.90
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root == None:
            return []
        stack = []
        p = root
        res = []
        while p or stack:
            if p != None:
                stack.append(p)
                p = p.left
                continue
            else:
                p = stack.pop()
                res.append(p.val)
                p = p.right
        return res