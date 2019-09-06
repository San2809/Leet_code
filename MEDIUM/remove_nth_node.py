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
        dumy = ListNode(0)
        dumy.next = head
        res =ListNode(0)
        res = head
        length =0
        while res:
            length +=1
            res = res.next
        length -=n
        res= dumy
        
        while length>0:
            length -=1
            res = res.next
        res.next = res.next.next
        return dumy.next