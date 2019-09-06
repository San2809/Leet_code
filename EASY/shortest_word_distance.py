class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        ans = float('inf')
        l = h = float('-inf')
        for i , w in enumerate(words):
            if w == word1:
                l = i
                ans = min(l-h, ans)
            elif w == word2:
                h = i
                ans = min(h-l, ans)
        return ans