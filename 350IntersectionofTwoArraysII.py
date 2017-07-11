#91.75
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        left1 = 0
        left2 = 0
        result = []
        while left1<len(nums1) and left2 < len(nums2):
            if nums1[left1] == nums2[left2]:
                result.append(nums1[left1])
                left1 += 1
                left2 += 1
            elif nums1[left1] <nums2[left2]:
                left1 += 1
            else:
                left2 += 1

        return result