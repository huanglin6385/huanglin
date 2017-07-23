#44.93
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if k >= len(nums1) * len(nums2):
            return [[i, j] for i in nums1 for j in nums2]
        visited = [[False] * len(nums2) for _ in range(len(nums1))]
        result = []
        stack = [[nums1[0] + nums2[0], 0, 0]]
        visited[0][0] = True
        while k:
            total_min, index_i, index_j = heapq.heappop(stack)
            result.append([nums1[index_i], nums2[index_j]])
            if index_i + 1 < len(nums1) and not visited[index_i + 1][index_j]:
                heapq.heappush(stack, [nums1[index_i + 1] + nums2[index_j], index_i + 1, index_j])
                visited[index_i + 1][index_j] = True
            if index_j + 1 < len(nums2) and not visited[index_i][index_j + 1]:
                heapq.heappush(stack, [nums1[index_i] + nums2[index_j + 1], index_i, index_j + 1])
                visited[index_i][index_j + 1] = True
            k -= 1

        return result
