class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        odd =0
        dic = {}
        for i in s:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i]%2 !=0:
                odd += 1
        return odd ==1 or odd==0