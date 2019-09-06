from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen, maxp,l, dic = 0, "", len(s), defaultdict(list)
        
        for i in range(l):
            dic[s[i]].append(i)
            for j in dic[s[i][::-1]]:
                if s[j:i+1] == s[j:i+1][::-1]:
                    if len(s[j:i+1])>maxlen:
                        maxlen = len(s[j:i+1])
                        maxp = s[j:i+1]
                        break
        return maxp