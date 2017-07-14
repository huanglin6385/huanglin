#44.41
#optimize root all nodes maxheight-minheight<=1  reteurn True  else isBalanced(sa follows)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        left_depth = self.depth(root.left, 0)
        right_depth = self.depth(root.right, 0)
        return abs(right_depth - left_depth) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root, height):
        if root == None:
            return height

        if root.left == None and root.right == None:
            return height + 1

        return max(self.depth(root.left, height + 1), self.depth(root.right, height + 1))