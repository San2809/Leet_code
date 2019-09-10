# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        
        old = head
        n = 1
        while old.next:
            old = old.next
            n +=1
        old.next = head
        new = head
        for i in range(n - k % n - 1):
            new = new.next
        newhead = new.next
        
        new.next =None
        return newhead
        