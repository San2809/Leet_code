class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact = 1
        for i in range(2, n + 1):
            fact = fact * i
        
   
        num = [i for i in range(1, n + 1)]
        res = [""] * (n) 
    
        i = 0
        while k > 1:
            fact = fact//n
            idx = (k - 1)//fact
            k = k - (idx) * fact
            res[i] = (str)(num[idx])
            i += 1
            num.pop(idx)
            n -= 1
        for n in num:
            res[i] = (str)(n)
            i += 1
            
        return "".join(res)