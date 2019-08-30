class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        
        if k>0:
            if k > l:
                k %= l
            nums[:] = nums[l-k:] + nums[:l-k]
                