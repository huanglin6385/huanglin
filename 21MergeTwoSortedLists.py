#75.95
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            head = ListNode(0)
            p = head
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    p = p.next
                    l1 = l1.next
                else:
                    p.next = l2
                    p = p.next
                    l2 = l2.next

            if l1:
                p.next = l1
            elif l2:
                p.next = l2

            return head
