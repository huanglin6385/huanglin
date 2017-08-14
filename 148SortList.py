#99.04
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        p = head
        while p:
            stack.append(p.val)
            p = p.next

        stack.sort()
        p = head
        index = 0
        while p:
            p.val = stack[index]
            index += 1
            p = p.next

        return head
