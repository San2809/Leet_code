class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>=len(t):
            h=s
            l=t
        else:
            h=t
            l=s
        dic = {}
        for i in h:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for i in l:
            if i in dic:
                dic[i] -=1
        for i in dic:
            if dic[i] !=0:
                return False
        return True
                
        