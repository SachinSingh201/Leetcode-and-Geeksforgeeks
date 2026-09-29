class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid)*len(grid)
        sn = n * (n+1 )//2
        s2n = n* (n+1)*(2*n +1) // 6
        xn = 0
        x2n = 0
        for i in range(m):
            for j in range(m):
                xn += grid[i][j]
                x2n += grid[i][j]*grid[i][j]

        
        a = sn-xn
        b = (s2n-x2n) //a 
        missing = (a+b)//2
        repeated = missing - a 
        return[repeated,missing]
