import collections

class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        a, b = [], []

        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    a.append((r, c))
                if img2[r][c]:
                    b.append((r, c))

        count = collections.Counter()
        ans = 0

        for r1, c1 in a:
            for r2, c2 in b:
                shift = (r2-r1, c2-c1)
                count[shift] += 1
                ans = max(ans, count[shift])

        return ans