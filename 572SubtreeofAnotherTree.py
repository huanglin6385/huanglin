#98.53
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None and t == None:
            return True
        elif s == None:
            return False
        elif t == None:
            return False
        elif s.val == t.val:
            if s.left == None and s.right == None and t.left == None and t.right == None:
                return True
            else:
                judge = self.is_True(s.left, t.left) and self.is_True(s.right, t.right)
                if judge:
                    return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_True(self, root, subtree):
        if root == None and subtree == None:
            return True
        elif root == None:
            return False
        elif subtree == None:
            return False
        elif root.val == subtree.val:
            return self.isSubtree(root.left, subtree.left) and self.isSubtree(root.right, subtree.right)
        return False