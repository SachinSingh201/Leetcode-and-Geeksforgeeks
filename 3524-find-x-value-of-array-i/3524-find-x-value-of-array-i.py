class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        cnt = [0] * k
        result = [0] * k
        
        for num in nums:
            a = num % k
            nxtcnt = [0] * k
            
           
            for m in range(k):
                mod = (m * a) % k
                nxtcnt[mod] += cnt[m]
                result[mod] += cnt[m]
                
            
            nxtcnt[a] += 1
            result[a] += 1
            
            
            cnt = nxtcnt
            
        return result