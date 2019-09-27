class Solution(object):
    def pivot(self, arr, low, high):
        if low<=high:
            mid = (low+high)/2
            if arr[mid]<arr[low]:
                return self.pivot(arr,low,mid)
            elif arr[mid]>arr[high]:
                return self.pivot(arr,mid+1,high)
            else:
                return low
    def bisearch(self, arr, l, h, key):
        if l>h:
            return -1
        mid = (l+h)/2
        if key >arr[mid]:
            return self.bisearch(arr,mid+1,h,key)
        elif key<arr[mid]:
            return self.bisearch(arr,l,mid-1,key)
        else:
            return mid
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n =len(nums)
        if n==0:
            return -1
        piv = self.pivot(nums,0,n-1)
        
        l1, h1 =0,(piv-1)%(n)
        l2, h2 = piv,n-1
        
        if nums[l1]<=target<=nums[h1]:
            return self.bisearch(nums,l1,h1,target)
        elif nums[l2]<=target<=nums[h2]:
            return self.bisearch(nums,l2,h2,target)
        else:
            return -1
        
        