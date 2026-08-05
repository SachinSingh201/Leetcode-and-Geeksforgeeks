# from collections import defaultdict

# class Solution(object):
#     def remainingMethods(self, n, k, invocations):
       
#         graph = defaultdict(list)
#         for u, v in invocations:
#             graph[u].append(v)

        
#         incoming = set()

#         for u in graph:
#             for v in graph[u]:
#                 incoming.add(v)

#         nonSuspicious = []

       
#         for u in graph:
#             if u not in incoming:
#                 nonSuspicious.append(u)
#                 nonSuspicious.extend(graph[u])

#         return nonSuspicious

from collections import defaultdict

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """

        graph = defaultdict(list)

        # Build graph
        for u, v in invocations:
            graph[u].append(v)

        
        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True

            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

       
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        ans = []

        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans