import fractions

class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 1000000007
        
    
        dp = {(0, 0): 1}
        
        for num in nums:
            ndp = dp.copy()
            for (g1, g2), val in dp.iteritems(): 
            
                ng1 = fractions.gcd(g1, num)
                ndp[(ng1, g2)] = (ndp.get((ng1, g2), 0) + val) % MOD
                
                ng2 = fractions.gcd(g2, num)
                ndp[(g1, ng2)] = (ndp.get((g1, ng2), 0) + val) % MOD
            dp = ndp
                
        ans = 0
        for (g1, g2), val in dp.iteritems():
            if g1 == g2 and g1 > 0:
                ans = (ans + val) % MOD
                
        return ans
