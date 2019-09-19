class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) < 3):
            return len(nums)
        i = 1    
        for j in xrange(2, len(nums)):
            if (nums[i-1] != nums[j]) or (nums[i] != nums[j]):
                i += 1        
            nums[i] = nums[j]   
        return i+1