#65.90
import collections
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = set([])
        two_sum = collections.defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                two_sum[nums[i]+nums[j]].append([i,j])


        visited = set([])

        for i in two_sum.keys():
            if i in visited or target-i in visited:
                continue
            if target - i in two_sum:
                for a in two_sum[target-i]:
                    for b in two_sum[i]:
                        res = a+b
                        if len(set(res)) <4 :
                            continue
                        res = tuple(sorted([nums[z] for z in res]))
                        result.add(res)
            visited.add(i)
            visited.add(target-i)



        return list(result)


test = Solution()
print test.fourSum([0,1,5,0,1,5,5,-4]
,11)