class Solution(object):
    def  __init__(self):
        self.stack = {}
    def getValue(self,k1):

        def binary_search(left,right,k):
            mid =