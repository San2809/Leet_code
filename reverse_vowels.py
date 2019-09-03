class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = {'a', 'e', 'i', 'o','u', 'A', 'E', 'I','O','U'}
        i =0
        j =len(s)-1
        s = list(s)
        while i<j:
            if s[i] in vow and s[j] in vow:
                s[i], s[j] = s[j], s[i]
                i +=1
                j -=1
            if s[i]  not in vow:
                i+= 1
            if s[j] not in vow:
                j -=1
        return "".join(s)
        