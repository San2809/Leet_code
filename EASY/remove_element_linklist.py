# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        temp = ListNode(0)
        temp.next = head
        prev = temp
        
        while head:
            if head.val == val:
                prev.next = head.next
                
                head = head.next
            else:
                head = head.next
                prev = prev.next
        return temp.next