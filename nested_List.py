class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def ds(nestedList, depth=1):
            return sum(depth*ni.getInteger() if ni.isInteger() else ds(ni.getList(), depth+1) for ni in nestedList)
        
        return ds(nestedList)