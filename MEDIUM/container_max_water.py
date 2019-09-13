class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxhigh, l, r = 0,0,len(height)-1
        while l<r:
            area = min(height[l],height[r])*(r-l)
            if area>maxhigh:
                maxhigh=area
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxhigh