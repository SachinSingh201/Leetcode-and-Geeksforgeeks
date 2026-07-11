class Solution:
    def countCompleteComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        self.V = self.E = 0

        def dfs(x):
            self.V += 1
            self.E += len(adj[x])
            visited[x] = True
            for nxt in adj[x]:
                if not visited[nxt]:
                    dfs(nxt)

        res = 0
        for i in range(n):
            if not visited[i]:
                self.V = self.E = 0
                dfs(i)
                if self.E == self.V * (self.V - 1):
                    res += 1

        return res