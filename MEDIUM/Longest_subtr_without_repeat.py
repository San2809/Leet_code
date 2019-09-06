class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans =0
        count =0
        i=0
        j=0
        lis =[]
        l =len(s)
        while j <l:
            
            if s[j] not in lis:
                lis.append(s[j])
                count =len(lis)
                if ans<count:
                    ans =count
                j +=1
            else:
                i +=1
                j =i
                count =0
                lis =[]
        return ans