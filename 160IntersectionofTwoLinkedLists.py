#84.77
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        lena = 1
        lenb = 1
        p = headA
        q = headB
        while p.next:
            lena += 1
            p = p.next
        while q.next:
            lenb += 1
            q = q.next
        if p.val != q.val:
            return None

        if lena > lenb:
            for _ in range(lena - lenb):
                headA = headA.next
        else:
            for _ in range(lenb - lena):
                headB = headB.next

        while headA.val != headB.val:
            headA = headA.next
            headB = headB.next

        return headA