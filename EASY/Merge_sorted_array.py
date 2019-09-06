def merge(nums1, m, nums2, n):

    i = m
    j = 0
    while(i<len(nums1) and j<len(nums2)):
            
        nums1[i] = nums2[j]
        i +=1
        j +=1
            
    return nums1.sort()

print(merge([1,2,3],3,[2,5,6],3))