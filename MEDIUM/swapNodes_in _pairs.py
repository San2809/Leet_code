# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        
        fst, scd = head, head.next
        rest = scd.next
        
        scd.next = fst
        fst.next = self.swapPairs(rest)
        return scd
        