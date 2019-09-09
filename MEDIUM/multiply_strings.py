class Solution(object):
    
    def multiply(self, num1, num2):
        dict = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        number1,number2 = 0,0
        len1 = len(num1)
        len2= len(num2)
        j=0
        for i in range(len1, 0,-1):
            number1 += (dict.get(num1[j]) * (10**(i-1)))
            j+=1
        j=0
        for i in range(len2, 0,-1):
            number2 += (dict.get(num2[j]) * (10**(i-1)))
            j+=1
        
        return str(number1*number2)