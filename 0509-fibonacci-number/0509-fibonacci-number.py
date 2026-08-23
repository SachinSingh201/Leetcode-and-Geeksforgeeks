class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        memo = [0, 1]
        for i in range(2, n+1):
            memo.append(memo[i-1]+memo[i-2])

        return memo[n]

        