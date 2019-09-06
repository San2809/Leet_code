class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = headA
        l2=headB
        
        while l1 is not l2:
            l1 = l1.next if l1 is not None else headB
            l2 = l2.next if l2 is not None else headA
        return l1