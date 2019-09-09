class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        if len(intervals)==1:
            return [intervals[0]]
        elif len(intervals)==0:
            return []
        l,r = intervals[0]
        res =[]
        for i in range(1, len(intervals)):
            cl,cr = intervals[i]
            if r<cl:
                res.append([l,r])
                l,r = cl,cr
            else:
                r = max(r,cr)
        res.append([l,r])
        return res