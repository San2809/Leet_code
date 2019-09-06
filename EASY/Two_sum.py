def twosum(nums, target):
    dict = {}
    for index, num in enumerate(nums):
        if(target-num in dict):
            return [dict.get(target-num), index]
        dict[num]=index

print(twosum(nums=[2,7,11,15], target=9))  

'''
factorial trail zeros
        f = math.factorial(n)
        cnt = 0
        while f%10 == 0:
            cnt +=1
            f /=10
        return cnt
'''