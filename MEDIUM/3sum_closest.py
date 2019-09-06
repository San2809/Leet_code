class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        res = sum(nums[:3])
        
        dif = abs(res-target)
        
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            
            while l<r:
                ans = nums[i]+nums[l]+nums[r]
                cur = abs(ans-target)
                
                if cur < dif:
                    dif =cur
                    res =ans
                if ans <target:
                    l +=1
                elif ans>target:
                    r -=1
                else:
                    return res
        return res
                    