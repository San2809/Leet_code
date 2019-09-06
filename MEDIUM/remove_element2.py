from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic ={}
        dic = collections.Counter(nums)
        
        for i in dic:
            if dic[i]>2:
                while dic[i] !=2:
                    nums.remove(i)
                    dic[i]-=1
        return len(nums)