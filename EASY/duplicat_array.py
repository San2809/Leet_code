def removeDuplicate(nums):

    #length = len(nums)

    if len(nums)==0:
        return 0
    cur=nums[0]
    pointer=0
    for i in range(1,len(nums)):
        if nums[i]!=cur:
            cur=nums[i]
            pointer+=1
            nums[pointer]=cur
    return nums

print(removeDuplicate([1,1,2,3]))
