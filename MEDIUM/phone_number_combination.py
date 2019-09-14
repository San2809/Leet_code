class Solution(object):
    def add_letters(self, words, letters):
        out =[]
        for l in letters:
            for w in words:
                out.append(w+l)
        return out
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = ['',
           '',
           'abc',
           'def',
           'ghi',
           'jkl',
           'mno',
           'pqrs',
           'tuv',
           'wxyz']
        
        
        if not digits:
            return []
        words =[""]
        
        for digit in digits:
            let = letters[int(digit)]
            words = self.add_letters(words,let)
        return words
        
        