#31.85
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        history = ListNode(0)
        history.next = head
        p = history
        while head:
            if head.val == val:
                history.next = head.next
                head = head.next
            else:
                history = head
                head = head.next

        return p.next