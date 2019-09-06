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
        curr = pre = ListNode(None)
        curr.next = head   
        dummy = pre   
        while curr and curr.next:
            if curr.val == curr.next.val:
                val = curr.val   
                while curr and curr.val == val:  
                    curr = curr.next
                pre.next = curr  
            else:  
                pre = curr
                curr = curr.next
        return dummy.next
                
        