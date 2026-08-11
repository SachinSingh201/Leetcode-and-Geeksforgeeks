from heapq import heappush, heappop


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)

        visited = set()

        # (weight, node)
        heap = [(0, 0)]

        cost = 0

        while heap and len(visited) < n:

            weight, u = heappop(heap)

            if u in visited:
                continue

            visited.add(u)
            cost += weight

            for v in range(n):

                if v not in visited:

                    x1, y1 = points[u]
                    x2, y2 = points[v]

                    distance = abs(x2 - x1) + abs(y2 - y1)

                    heappush(heap, (distance, v))

        return cost