# class Solution(object):
#     def shiftGrid(self, grid, k):
#         n = len(grid)
#         m = len(grid[0])

#         arr = []

#         for row in grid:
#             arr.extend(row)

#         k %= (n * m)

#         arr = arr[-k:] + arr[:-k]

#         ans = []

#         idx = 0
#         for i in range(n):
#             ans.append(arr[idx:idx+m])
#             idx += m

#         return ans

class Solution(object):
    def shiftGrid(self, grid, k):
        n = len(grid)
        m = len(grid[0])

        total = n * m
        k %= total

        while k:
            curr = grid[n-1][m-1]

            for i in range(n):
                for j in range(m):
                    grid[i][j], curr = curr, grid[i][j]

            k -= 1

        return grid