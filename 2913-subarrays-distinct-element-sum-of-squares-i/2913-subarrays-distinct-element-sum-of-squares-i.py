class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0 
        for i in range(len(nums)):
            for j in range(len(nums)):
                part = nums[i:j+1]
                xSum = len(set(part))
                ans+= xSum**2
        return ans
        