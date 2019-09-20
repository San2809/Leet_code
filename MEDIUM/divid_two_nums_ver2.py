class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        intmax , intmin = 2147483647, -2147483648
        
        if divisor == 0:
            return intmax
        if dividend == intmin:
            if divisor == 1:
                return intmin
            elif divisor ==-1:
                return intmax
        sign =1
        
        if divisor*dividend <0:
            sign = -1
        divisor , dividend = abs(divisor), abs(dividend)
        
        quo =0
        
        while dividend >= divisor:
            shift =0
            while dividend >=(divisor<<shift):
                shift +=1
            dividend -= divisor<<(shift-1)
            quo += 1<<(shift-1)
        if sign*quo < intmin or sign*quo > intmax:
            return intmax
        else:
            return sign*quo
        