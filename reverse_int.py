class Solution(object):
    def reverse(self, x):
        if(-2**31<x<0):
            x=x*-1
            rev = 0
            while(x!=0):
                pop = x % 10
                x = x//10
                rev = rev*10 + pop
            rev = rev*-1
        elif(0<=x<2**31):
            rev = 0
            while(x!=0):
                pop = x % 10
                x = x//10
                rev = rev*10 + pop
        else:
            rev=0
        return rev
        