class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n ==0:
            return []
        if k==0:
            return [[]]
        
        arr =[]
        for i in range(1,n+1):
            arr.append(i)
        
        res = itertools.combinations(arr,k)
        return res
        