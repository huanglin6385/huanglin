#76.36
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        def issame(L,R):
            if L == None and R == None:
                return True
            if L and R and L.val == R.val:
                return issame(L.left,R.right) and issame(L.right,R.left)
            return False

        return issame(root.left,root.right)
