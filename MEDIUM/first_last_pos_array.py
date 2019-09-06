class Solution(object):
    def idx(self, nums, target, left):
        i=0
        j=len(nums)
        while i<j:
            
            
            mid = (i+j)//2
            if nums[mid]>target or (left and target == nums[mid]):
                
                j=mid
                
            else:
                i = mid+1
        return i
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_idx = self.idx(nums, target, True)
        
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1,-1]
        
        return [left_idx, self.idx(nums, target, False)-1]