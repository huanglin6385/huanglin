#99.55
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random
class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.stack = []
        p = head
        while p:
            self.stack.append(p.val)
            p = p.next


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return random.choice(self.stack)



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(head)
        # param_1 = obj.getRandom()