class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=1:
            return "1"
        
        a ="1"
        
        for _ in range(n-1):
            c =0
            b =""
            temp = a[0]
            
            for j in a:
                if j == temp:
                    c +=1
                else:
                    b = b + str(c) + str(temp)
                    temp = j
                    c =1
            b = b+str(c)+str(j)
            a = b
        return a