class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ranset = set(ransomNote)
        for i in ranset:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True