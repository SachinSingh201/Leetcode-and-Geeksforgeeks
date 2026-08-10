from heapq import heappop, heappush


class Solution(object):
    def networkDelayTime(self, edges, n, s):
        """
        :type edges: List[List[int]]
        :type n: int
        :type s: int
        :rtype: int
        """

        adjlst = []

        for i in range(n):
            adjlst.append([])

        for edge in edges:
            x = edge[0] - 1
            y = edge[1] - 1
            w = edge[2]

            adjlst[x].append((y, w))

        s -= 1

        heap = []

        dist = [float("inf")] * n
        dist[s] = 0

        heappush(heap, (dist[s], s))

        while heap:
            d, u = heappop(heap)

            
            if d > dist[u]:
                continue

            for v, w in adjlst[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(heap, (dist[v], v))

        ans = max(dist)

        if ans == float("inf"):
            return -1

        return ans