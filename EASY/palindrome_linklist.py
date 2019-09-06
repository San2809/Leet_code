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
        if not head: return True
        
        slow = fast  = head
        
        while fast is not None and fast.next is not None: #fast to end and slow to middle
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
            
        while prev:
            if prev.val !=head.val:
                return False
            
            prev = prev.next
            head = head.next
            
        return True
            
            
        
            