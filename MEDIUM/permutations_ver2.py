class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        N = len(nums)
        if N == 1:
            return [nums]
        elif N == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        else:
            res = []
            for i in range(N):
                pert = self.permute(nums[0:i] + nums[i+1:N])
                for p in pert:
                    res.append([nums[i]]+p)
            return res
        