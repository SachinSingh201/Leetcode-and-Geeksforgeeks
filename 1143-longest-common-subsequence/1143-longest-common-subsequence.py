class Solution(object):

    def rec(self,i,j,text1,text2,dp):
        if i >= len(text1) or j >= len(text2):
            return 0 
        if dp[i][j] != -1:
            return dp [i][j]


        if text1[i] == text2[j]:
            dp[i][j]  = 1+self.rec(i+1,j+1,text1,text2,dp)
        else:
           dp [i][j]  = max(self.rec(i+1,j,text1,text2,dp) , self.rec(i,j+1,text1,text2,dp))

        return dp [i][j]
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # n = len(text1)
        # m = len(text2)

        # dp = [[0 for _ in range(m+1)] for k in range(n+1)]

        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = 1+dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        # return dp[n][m]
        n = len(text1)
        m = len(text2)

        dp = [[-1 for _ in range(m)] for k in range(n)]

        return self.rec(0,0,text1,text2,dp)

    