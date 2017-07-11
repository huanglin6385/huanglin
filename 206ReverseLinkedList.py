#93.03
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        head_next = head.next
        head.next = None
        while head_next:
            head_next_next = head_next.next
            head_next.next = head
            head = head_next
            head_next = head_next_next

        return head
