#37.73
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 or m == 0:
            if n == 0:
                nums1[:] = nums2[:]
            return
        m -= 1
        n -= 1
        for i in xrange(m + n + 1, -1, -1):
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
                if m<0:
                    nums1[:n+1] = nums2[:n+1]
                    return
            else:
                nums1[i] = nums2[n]
                n -= 1
                if n<0:
                    return