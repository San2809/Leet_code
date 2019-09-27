# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        s = f =head
        while n>0 and f:
            f = f.next
            n-=1
        
        if not f:
            return head.next
        
        while f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return head
        
        