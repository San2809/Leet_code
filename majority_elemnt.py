class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        n = len(nums)//2
        
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] >n:
                return i
        