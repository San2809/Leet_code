def Lcp(str1,str2):
    result = ""
    j=0
    i=0
    while(i<len(str1) and j<len(str2)):
        if(str1[i]!=str2[j]):
            break
        result = result+str1[i]
        i+=1
        j+=1
    return result

def longestCommonPrefix(strs):
    
    res=""
    if(len(strs)==0):
        res=""
    elif(len(strs)==1):
        res=strs[0]
    else:
        temp = strs[0]
        i=1
        while(i<len(strs)):
            res = Lcp(temp,strs[i])
            temp =res
            i+=1
    return res

print(longestCommonPrefix(["flower","dog","floght"]))




