#30.13
import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        for dot1, dot2 in edges:
            graph[dot1].add(dot2)
            graph[dot2].add(dot1)

        def maxpath(node, visited):
            visited.add(node)
            paths = [maxpath(dot, visited) for dot in graph[node] if dot not in visited]
            path = max(paths or [[]], key=len)
            path.append(node)
            return path

        path = maxpath(0,set())
        path = maxpath(path[0],set())
        return path[(len(path) - 1) / 2:len(path) / 2 + 1]



test = Solution()
print test.findMinHeightTrees(7,[[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]])