class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        counts = {}
        for i, v in enumerate(nums):
            if v in counts:
                if i - counts[v] <= k:
                    return True
                else:
                    counts[v] = i
            else:
                counts[v] = i
        return False