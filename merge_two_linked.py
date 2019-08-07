def mergeTwoLists(l1: ListNode, l2:ListNode)-> LsitNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prehead = ListNode(-1)
        while l1 and l2:
            if l1.val<=l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                pev.next = l2
                l2 = l2.next
            prev = prev.next
        
        prev.next = l1 if l1 is not None else l2
        
        return prehead.next

print(mergeTwoLists([1,3,4], [1,2,5]))