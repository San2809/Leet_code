def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    if not a and not b:
        return "0"
        
    elif not a:
        return b
        
    elif not b:
        return a
        
    else:
        return bin(int(a,2) + int(b,2))[2:]