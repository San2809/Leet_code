class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        l1, l2, cur = 1, 1, 0
        for i in range(1, len(s)):
            if s[i] != '0':
                cur = l1
            if '10' <= s[i - 1: i + 1] <= '26':
                cur += l2
            l1, l2, cur = cur, l1, 0
        return l1
        