class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        if n <= 999:
            return ans

        else :
            ans = n - 999
        return ans    
        