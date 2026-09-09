class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        
        lower = 1000
        commas = 1
        
        while n >= lower:
           
            upper = lower * 1000 - 1
            
            
            count = min(n, upper) - (lower - 1)
            
            
            ans += count * commas
            
           
            lower *= 1000
            commas += 1
        
        return ans