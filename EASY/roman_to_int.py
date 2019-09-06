def value(x):
    if(x=='I'):
        return 1
    if(x=='V'):
        return 5
    if(x=='X'):
        return 10
    if(x=='L'):
        return 50
    if(x=='C'):
        return 100
    if(x=='D'):
        return 500
    if(x=='M'):
        return 1000
def romantoInt(s):
    res =0
    i=0
    while(i<len(s)):
        s1 =value(s[i])
        if(i+1<len(s)):
            s2 =value(s[i+1])
            
            if(s1>=s2):
                res =res+s1
                i=i+1
            else:
                res=res+s2-s1
                i=i+2
        else:
            res=res+s1
            i=i+1
    return res

print(romantoInt("MCMIV"))