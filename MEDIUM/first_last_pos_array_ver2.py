class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l =0
        r =len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                left = mid
                right = mid
            
                while(True):
                    if left<l or nums[left]!=target:
                        left+=1
                        break
                    left-=1
                
                while(True):
                    if right>r or nums[right]!=target:
                        right -=1
                        break
                    right +=1
                return [left,right]
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return [-1,-1]
            
            