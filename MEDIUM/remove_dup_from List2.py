# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        
        prev = dummy = ListNode(9999999)
        dummy.next = curr = head
        check = prev.val
        
        while curr:
            if curr.val == check:
                prev.next = curr.next
                curr = curr.next
                continue
            if curr.next and curr.val ==curr.next.val:
                check = curr.val
                continue
            prev, curr = curr, curr.next
            check = prev.val
        return dummy.next 