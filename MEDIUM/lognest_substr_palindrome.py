class Solution(object):
    def helper(self,s,l,r):
        while l>=0 and r<len(s):
            if s[l] !=s[r]:
                break
            l -=1
            r +=1
        return [l+1,r]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr = [0,1]
        
        for i in range(len(s)):
            even = self.helper(s,i-1,i)
            odd = self.helper(s,i-1,i+1)
            
            longest = max(even,odd, key=lambda X: X[1]-X[0])
            curr = max(curr,longest, key =lambda X:X[1]-X[0])
            
        return s[curr[0]:curr[1]]