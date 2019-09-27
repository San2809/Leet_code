class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        
        for s in strs:
            sort = ''.join(sorted(s))
            if sort in dic:
                dic[sort].append(s)
            else:
                dic[sort] = [s]
        return dic.values()
        