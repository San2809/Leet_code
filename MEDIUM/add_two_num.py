# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 =""
        num2 =""
        
        while l1 != None:
            num1 = str(l1.val)+num1
            l1 =l1.next
        while l2!=None:
            num2 = str(l2.val)+num2
            l2 =l2.next
        
        idx =1
        sum = str(int(num1)+int(num2))
        root =ListNode(sum[0])
        
        while idx<len(sum):
            newRoot = ListNode(sum[idx])
            
            newRoot.next =root
            root =newRoot
            idx +=1
        return root

            
        