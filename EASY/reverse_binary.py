class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = '{0:032b}'.format(n)
        return int(s[::-1], 2)
        