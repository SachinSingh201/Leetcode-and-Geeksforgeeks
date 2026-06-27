from collections import Counter

class Solution: 
    def maximumLength(self, nums): 
        freq = Counter(nums) 
        res = (freq.pop(1, 0) - 1) | 1 
        
        for f in freq: 
            x = f 
           
            sq = int(x ** 0.5) 
            if sq * sq == x and freq.get(sq, 0) > 1: 
                continue 
            
            n = 0 
            while x < 31623 and freq.get(x, 0) > 1: 
                n += 2 
                x *= x 
            
            res = max(res, n + ((x in freq) << 1) - 1) 
            
        return res
