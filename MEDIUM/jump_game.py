class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)> 1 and nums[0]==0:
            return False
        elif len(nums)==0:
            return True
        flag = False
        length = 2
        for i in range(len(nums)-2, -1, -1):
            if not flag and nums[i]==0:
                flag = True
            if flag and i-1>=0 and nums[i-1]>=length:
                length = 2
                flag = False
            elif flag:
                length +=1
        return not flag