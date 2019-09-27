class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        n = len(nums)
        max_step = 0

        for i in range(n):
            if max_step < i:
                return False
            max_step = max(max_step, i + nums[i])

        return max_step >= n - 1
        