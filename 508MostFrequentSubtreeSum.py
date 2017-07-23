#74.63
import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dict1 = collections.defaultdict(int)

        def dfs(root):
            if root == None:
                return 0

            now = root.val + dfs(root.left) + dfs(root.right)
            dict1[now] += 1
            return now

        dfs(root)
        most_occur = 0
        result = []
        for i in dict1:
            if dict1[i] > most_occur:
                most_occur = dict1[i]
                result = [i]
            elif dict1[i] == most_occur:
                result.append(i)

        return result
