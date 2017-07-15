#51.17
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        p = ListNode(-1)
        p.next = head
        two_p = p
        while two_p and two_p.next:
            two_p = two_p.next.next
            p = p.next

        history = p
        p = p.next
        history.next = None
        while p:
            p_next = p.next
            p.next = history
            history = p
            p = p_next

        while history != None and head != None:
            if history.val != head.val:
                return False

            history = history.next
            head = head.next

        return True