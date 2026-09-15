class Solution(object):
    def maxPalindromes(self, s, k):
       

        n = len(s)

        
        isPalindrome = [[False] * n for _ in range(n)]

        
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                isPalindrome[left][right] = (
                    s[left] == s[right] and
                    (length <= 2 or isPalindrome[left + 1][right - 1])
                )

        
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            
            dp[i] = dp[i - 1]

            
            for j in range(i - k + 1):
                if i - j >= k and isPalindrome[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]