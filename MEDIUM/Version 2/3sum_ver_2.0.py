class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        leng =len(nums)
        if leng==3:
            if sum(nums)==0:
                return [nums]
        if leng<3:
            return []
        if leng>3:
            res =[]
            nums.sort()
            for i in range(leng-2):
                l, r = i+1, leng-1
                if i>0 and nums[i]==nums[i-1]:
                    continue
                while l<r:
                    s= nums[i]+nums[l]+nums[r]
                    
                    if s<0:
                        l+=1
                    elif s>0:
                        r-=1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        
                        while l<r and nums[l]==nums[l+1]:
                            l +=1
                        while l<r and nums[r]==nums[r-1]:
                            r -=1
                        
                        l +=1
                        r -=1
            return res
        