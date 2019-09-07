class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l ==1: return
        
        for i in range(l-2, -1, -1):
            if nums[i]< nums[i+1]:
                break
        if i ==0 and nums[0]>=nums[1]:
            s =0
            e = l-1
        else:
            tag =i
            while i <l -1 and nums[tag]<nums[i+1]:
                i +=1
            replace = i
            nums[tag], nums[replace] = nums[replace], nums[tag]
            
            s = tag +1
            e = len(nums) -1
            
        while s< e:
            nums[s], nums[e] = nums[e], nums[s]
            s +=1
            e -=1
        
            
    
        