class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = set(nums)
        val = 1 
        while True:
            if val*k not in nums:
                return val*k
            val+=1
            
        

        