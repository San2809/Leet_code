class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [True]*n
        
        if n<2:
            return 0
        else:
            prime[0] = prime[1] = False
        
        for i in range(2, n):
            if prime[i] is not False:
                for j in range(i*i, n, i):
                    prime[j] = False
        return sum(prime)
            
        
        