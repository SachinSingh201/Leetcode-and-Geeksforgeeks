from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        empty , fresh , rotten = 0,1,2

        m = len(grid) 
        n = len(grid[0])
        freshCount = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == rotten:
                    q.append((i,j))
                elif grid[i][j] == fresh:
                    freshCount+=1
        if freshCount == 0:
            return 0
        
        num_minutes = -1
        while q:
            length = len(q)
            num_minutes +=1
            for _ in range(length):
                i,j = q.popleft()
                for r,c in [(i+1,j) ,(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<= r <m and 0<= c <n and grid[r][c] == fresh:
                        grid[r][c] = rotten
                        freshCount -=1
                        q.append((r,c))
        if freshCount == 0:
            return num_minutes
        else:
            return -1
        