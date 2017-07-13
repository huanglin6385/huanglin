#93.88
import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        self.result = 0

        def dfs(root, dict1, total_now, target):
            if root == None:
                return
            if root.val + total_now - target in dict1:
                self.result += dict1[root.val + total_now - target]

            dict1[total_now + root.val] += 1
            dfs(root.left, dict1, total_now + root.val, target)
            dfs(root.right, dict1, total_now + root.val, target)
            dict1[total_now + root.val] -= 1

        dict1 = collections.defaultdict(int)
        dict1[0] = 1
        dfs(root,dict1,0,sum)
        return self.result

