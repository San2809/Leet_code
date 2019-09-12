class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        t=target
        if nums is None or len(nums)==0:
            return False
        l = 0
        r = len(nums)-1
        
        while l<=r:
            p = (l+r)/2
            
            if nums[l]==t or nums[r]==t or nums[p]==t:
                return True
            if nums[l]<nums[r]:
                if t<nums[l] or t>nums[r]:
                    return False
                if t<nums[p]:
                    r =p-1
                else:
                    l =p+1
            else:
                if nums[l]<nums[p] and nums[l]<t and t<nums[p]:
                    r = p-1
                elif nums[p]<nums[r] and t<nums[r] and t>nums[p]:
                    l =p+1
                else:
                    p -=1
                    l+=1
        return False
                
        