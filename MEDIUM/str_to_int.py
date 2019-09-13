class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.lstrip()
        if(len(str)==0):
            p = 0
        elif(str[0]=="-" or str[0]=="+"):
            i = 1
            if(len(str)>1):
                while(i<len(str) and str[i] in "0123456789"):
                    i+=1
                if(i>1):
                    p = (int(str[0:i]))
                else:
                    p = 0
            else:
                p = 0
        elif(str[0] in "0123456789"):
            i = 1
            if(len(str)>1):
                while(i<len(str) and str[i] in "0123456789"):
                    i+=1
                p = int(str[0:i])
            else:
                p = (int(str))
        else:
            p = 0
        z = 2**31
        if(p>=z):
            p = z-1
        elif(p<-z):
            p = -z
        return p
            
