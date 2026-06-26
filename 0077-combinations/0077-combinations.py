class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs (curr,arr):
            if len(arr) == k:
                ans.append(arr[:])
                return 
            if curr > n:
                return n
            arr.append(curr)
            dfs(curr+1,arr)

            arr.pop()
            dfs(curr+1,arr)
        dfs(1,[])
        return ans

        