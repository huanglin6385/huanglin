# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 =[]
        while l1:
            p1.append(l1.val)
            l1 = l1.next

        p2 = []
        while l2:
            p2.append(l2.val)
            l2 = l2.next

        p = None
        history = 0
        if len(p1) < len(p2):
            p1 = [0]*(len(p2)-len(p1)) + p1
        else:
            p2 = [0]*(len(p1)-len(p2)) + p2

        for i,j in zip(p1[::-1],p2[::-1]):
            number = i+j+history
            root = ListNode(number%10)
            root.next = p
            p = root
            history = number/10
        if history== 0:
            return p

        root = ListNode(history)
        root.next = p
        return root