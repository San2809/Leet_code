class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        l = len(intervals)
        i =0
        
        while i+1 <l:
            if intervals[i+1][0]<=intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
                l-=1
            else:
                i+=1
        return intervals