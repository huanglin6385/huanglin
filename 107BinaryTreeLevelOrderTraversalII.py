#68.17
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def binary_search(root,level):
            if root == None:
                return
            if len(result) < level + 1:
                result.append([])
            result[level].append(root.val)
            binary_search(root.left,level + 1)
            binary_search(root.right,level + 1)

        binary_search(root,0)
        return result[::-1]