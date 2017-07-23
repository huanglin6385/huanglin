import collections
def array_partin(nums,length):
    dict1 = collections.defaultdict(list)
    dict1[nums[0]] = [0]
    for i in range(1,length):
        nums[i] += nums[i-1]
        dict1[nums[i]].append(i)



    count = 0
    min_number = nums[length-1]/3
    max_number = min_number+1
    p = set([min_number,max_number])

    for k in range(2*min_number,2*min_number+4):
        if dict1.has_key(k):
            stack_2_3 = dict1[k]
            for number in [min_number,max_number]:
                if dict1.has_key(number):
                        s1 = number
                        s2 = k-number
                        s3 = nums[length-1] - k
                        if s1 in p and s2 in p and s3 in p:
                            stack_1_3 = dict1[number]
                            left_1 = 0
                            left_2 = 0
                            while left_1 <len(stack_1_3) and left_2 < len(stack_2_3):
                                if stack_1_3[left_1] < stack_2_3[left_2]:
                                    left_1 += 1
                                else:
                                    count += left_1
                                    left_2 += 1
                            count += (len(stack_2_3)-left_2)*left_1

    return count


print array_partin([0,0,0,0,0],5)
