class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        plist = [p for p in path.split('/') if p]
        stack = []
        
        for p in plist:
            if p == '..':
                if stack: stack.pop()
            elif p != '.':
                stack.append(p)
        return '/'+'/'.join(stack)