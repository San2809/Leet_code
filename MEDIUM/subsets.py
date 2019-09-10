class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        out = []
        for i in range(2**len(nums)):
            bitset = reversed(list(format(i, 'b')))
            iset = []
            for idx, bit in enumerate(bitset):
                if (bit == '1'):
                    iset.append(nums[idx])
            out.append(iset)
        return out
        