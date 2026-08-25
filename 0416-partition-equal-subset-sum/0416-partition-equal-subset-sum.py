class Solution(object):
    def rec(self, i, curr_sum, nums, dp):

        target = self.total // 2

        if curr_sum == target:
            return True

        if curr_sum > target or i >= len(nums):
            return False

        if dp[i][curr_sum] != -1:
            return dp[i][curr_sum]

        take = self.rec(
            i + 1,
            curr_sum + nums[i],
            nums,
            dp
        )

        noTake = self.rec(
            i + 1,
            curr_sum,
            nums,
            dp
        )

        dp[i][curr_sum] = take or noTake

        return dp[i][curr_sum]

    def canPartition(self, nums):
        n = len(nums)

        self.total = sum(nums)

        if self.total % 2 != 0:
            return False

        target = self.total // 2

        dp = [[-1 for _ in range(target + 1)]
              for _ in range(n)]

        return self.rec(0, 0, nums, dp)