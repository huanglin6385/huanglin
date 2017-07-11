#87.78
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.uniqueanddiameter(root, 1)[1]-1

    def uniqueanddiameter(self,root,result):
        diameter = result
        if root.left == None and root.right == None:
            return 1,diameter
        elif root.left == None:
            right_result = self.uniqueanddiameter(root.right,diameter)
            unique = right_result[0] + 1
            diameter = max(right_result[1],diameter,right_result[0] + 1)
        elif root.right == None:
            left_result = self.uniqueanddiameter(root.left,diameter)
            unique = left_result[0] + 1
            diameter = max(left_result[1], diameter,left_result[0] + 1)
        else:
            right_result = self.uniqueanddiameter(root.right,diameter)
            left_result = self.uniqueanddiameter(root.left,diameter)
            unique = max(left_result[0],right_result[0]) + 1
            diameter = max(diameter,left_result[1],right_result[1],left_result[0]+right_result[0] + 1)

        return [unique,diameter]