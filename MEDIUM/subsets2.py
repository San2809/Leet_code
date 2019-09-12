class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, pos, nums = [[]], {}, sorted(nums)
        for n in nums:
            frm, ln = pos.get(n, 0), len(ans)
            for ls in ans[frm:]:
                ans.append(ls + [n])
            pos[n] = ln
        
        return ans