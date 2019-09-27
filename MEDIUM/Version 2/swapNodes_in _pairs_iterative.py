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
        cur, pre = head, None
        while cur and cur.next:
            
        
            fst , scd, trd = cur, cur.next, cur.next.next
        
            fst.next = trd
            scd.next = fst
            
            if not pre:
                head = scd
            else:
                pre.next = scd
                
            pre = fst
            cur = trd
        return head
        