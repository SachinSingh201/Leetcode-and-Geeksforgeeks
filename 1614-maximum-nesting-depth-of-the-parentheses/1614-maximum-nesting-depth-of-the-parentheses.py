class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        current = 0 
        
        for ch in s:
            if ch =="(" :
                current+=1
            elif ch == ")":
                current -=1
            ans = max(ans,current)
        return ans 


        