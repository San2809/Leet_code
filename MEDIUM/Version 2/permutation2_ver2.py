class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.perms = []
        nums.sort()
        def backtrack(n, current_perm):
            if not n:
                self.perms.append(current_perm)
                return
            for i in range(0, len(n)):
                if (i > 0 and n[i - 1] != n[i]) or i == 0:
                    backtrack(n[:i] + n[i + 1:], current_perm + [n[i]])
        backtrack(nums, [])
        return self.perms