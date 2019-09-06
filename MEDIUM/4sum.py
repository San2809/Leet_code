class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if not nums: return []
        L, s ,N, M = len(nums), set(), {j:i for i,j in enumerate(nums)}, nums[-1]
        
        for i in range(L-3):
            a = nums[i]
            
            if a + 3*M <target: continue
            if 4*a >target: break
            
            for j in range(i+1, L-2):
                b = nums[j]
                if a + b + 2*M <target: continue
                if a + 3*b >target: break
                
                for k in range(j+1, L-1):
                    c = nums[k]
                    d = target - (a+b+c)
                    
                    if d > M: continue
                    if d < c: break
                    
                    if d in N and N[d] > k:
                        s.add((a,b,c,d))
        return s
                    
                    
                    
        