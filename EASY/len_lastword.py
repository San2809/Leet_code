def lengthofLastWord(s):
    split = s.split()
    if(len(split)==0): return 0
    return len(split[-1])
print(lengthofLastWord("hello world this is python"))