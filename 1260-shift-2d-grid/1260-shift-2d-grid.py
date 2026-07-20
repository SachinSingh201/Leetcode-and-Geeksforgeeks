class Solution(object):
    def shiftGrid(self, grid, k):
        n = len(grid)
        m = len(grid[0])

        arr = []

        for row in grid:
            arr.extend(row)

        k %= (n * m)

        arr = arr[-k:] + arr[:-k]

        ans = []

        idx = 0
        for i in range(n):
            ans.append(arr[idx:idx+m])
            idx += m

        return ans