# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        if head == None or head.next == None:
            return False
        while head and p and p.next:
            head = head.next
            p = p.next.next
            if head == p :
                return True

        return False