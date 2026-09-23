class Solution(object):
    def rec(self,i,nums,dp):
        if i >= len(nums):
            return 0 
        if dp[i] != -1:
            return dp[i]
        take = nums[i] + self.rec(i+2,nums,dp)

        nonTake = self.rec(i+1,nums,dp)

        dp[i] = max(take,nonTake)
        return dp[i]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1]*len(nums)
        return self.rec(0,nums,dp)
