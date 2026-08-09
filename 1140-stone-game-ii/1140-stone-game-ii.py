class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        memo = [[0] * (n + 1) for _ in range(n)]

        suffix_sum = piles[:]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        def max_stones(curr_index, M):

            
            if curr_index + 2 * M >= n:
                return suffix_sum[curr_index]

           
            if memo[curr_index][M] > 0:
                return memo[curr_index][M]

           
            res = float('inf')

            for X in range(1, 2 * M + 1):
                res = min(
                    res,
                    max_stones(
                        curr_index + X,
                        max(M, X)
                    )
                )

           
            memo[curr_index][M] = suffix_sum[curr_index] - res

            return memo[curr_index][M]

        return max_stones(0, 1)