class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {"1":"1", "0":"0", "6":"9", "9":"6", "8":"8"}
        
        ans = []
        for i in range(len(num)):
            if num[i] not in dic:
                return False
            else:
                if dic[num[i]] != num[len(num)-i-1]:
                    return False
        return True
        