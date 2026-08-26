class Solution(object):

    def rec(self, i, amount, coins, dp):

        if amount == 0:
            return 0

        if amount < 0 or i >= len(coins):
            return float('inf')

        if dp[i][amount] != -1:
            return dp[i][amount]

    
        take = 1 + self.rec(
            i,
            amount - coins[i],
            coins,
            dp
        )


        not_take = self.rec(
            i + 1,
            amount,
            coins,
            dp
        )

        dp[i][amount] = min(take, not_take)

        return dp[i][amount]

    def coinChange(self, coins, amount):
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        ans = self.rec(0, amount, coins, dp)

        if ans == float('inf'):
            return -1

        return ans