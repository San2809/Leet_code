def strStr(haystack, needle):

    if(len(needle)==0):
        return 0
        #res = -1
        
    for i in range(len(haystack)-len(needle)+1):
        if(haystack[i:i+len(needle)]==needle):
                #res = i
            return i
                
    return -1
print*(strStr("hello","ll"))

