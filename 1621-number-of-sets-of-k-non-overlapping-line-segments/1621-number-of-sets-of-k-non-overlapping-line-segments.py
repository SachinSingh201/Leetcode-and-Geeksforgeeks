class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        total = n + k - 1
        need = 2 * k

        dp = [[0] * (need + 1) for _ in range(total + 1)]

       
        for i in range(total + 1):
            dp[i][0] = 1

        for i in range(1, total + 1):
            for j in range(1, need + 1):

                # Not Take current position
                notTake = dp[i - 1][j]

                # Take current position
                take = dp[i - 1][j - 1]

                dp[i][j] = (take + notTake) % MOD

        return dp[total][need]