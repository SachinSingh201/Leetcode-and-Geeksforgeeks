from collections import deque

class Solution(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
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

        return len(ans) ==n
        


        
        