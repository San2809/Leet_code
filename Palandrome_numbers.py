'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
'''
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        #res=True
        temp=x
        if(x<0):
            return False
        
        rev = 0
         
        while(x!=0):
            pop = x % 10
            x = x//10
            rev = rev*10 + pop
        print(rev) 
        

        
        if(rev==temp):
            return True
        
        else:
            return  False
        
'''
 class Solution:
    def isPalindrome(self, x):
        x=str(x)
        if x[::-1]==x:
            return True
        else:
            return False
'''       
        
print(isPalindrome(-121))