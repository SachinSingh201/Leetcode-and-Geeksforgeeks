class Solution(object):
    def numIslands(self, grid):

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        ans = 0

        def dfs(r, c):

            if r < 0 or r >= m or c < 0 or c >= n:
                return

           
            if grid[r][c] == '0':
                return

          
            grid[r][c] = '0'

          
            dfs(r - 1, c)

           
            dfs(r + 1, c)

         
            dfs(r, c - 1)

          
            dfs(r, c + 1)

        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1':

                    
                    ans += 1

                   
                    dfs(i, j)

        return ans