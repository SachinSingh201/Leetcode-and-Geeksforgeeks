from collections import deque

class Solution(object):
    def findOrder(self, n, prerequisites):
       
        q = deque()
        adjlst = [[] for _ in range(n)]
        ans = []
        indegree =  [0]*n
        
        for a , b in  prerequisites:
            indegree[a] += 1
            adjlst[b].append(a)
        
        for z in range(n):
            if indegree[z] == 0:
                ans.append(z)
                q.append(z)

        while q:
            front = q.popleft()

            for x in adjlst[front]:
                indegree[x] -=1
                if indegree[x] == 0:
                    q.append(x)
                    ans.append(x)

        if len(ans) ==n:
            return ans
        return []