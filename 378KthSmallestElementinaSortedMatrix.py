#31.65
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
        stack = [[matrix[0][0], 0, 0]]
        visited[0][0] = False
        while k:
            min_now, index_i, index_j = heapq.heappop(stack)
            if index_i + 1 < len(matrix) and not visited[index_i + 1][index_j]:
                heapq.heappush(stack, [matrix[index_i + 1][index_j], index_i + 1, index_j])
                visited[index_i + 1][index_j] = True
            if index_j + 1 < len(matrix[0]) and not visited[index_i][index_j + 1]:
                heapq.heappush(stack, [matrix[index_i][index_j + 1], index_i, index_j + 1])
                visited[index_i][index_j + 1] = True
            k -= 1

        return min_now