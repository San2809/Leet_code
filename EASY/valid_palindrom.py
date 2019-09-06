def isPalindrom(s):

    st =''.join(ch.lower() for ch in s if ch.alnum())

    return st == st[::-1]