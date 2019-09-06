def plusOne(digits):
       
    s = ''.join([str(c) for c in digits])
    n = str(int(s) + 1)
    return list(n)

print(plusOne([1,2,9]))