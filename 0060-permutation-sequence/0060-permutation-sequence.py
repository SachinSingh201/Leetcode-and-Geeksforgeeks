# class Solution(object):
#     def getPermutation(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """
#         nums = [str(i) for i in range(1,n+1)]
#         used = [False]*n
#         result = []
#         def backtrack(path):
#             if len(path) == n:
#                 result.append("".join(path))
#                 return 
#             for i in range(n):
#                 if used[i]:
#                     continue
#                 used[i] = True

#                 path.append(nums[i])

#                 backtrack(path)
#                 path.pop()

#                 used[i] = False


class Solution(object):
    def getPermutation(self, n, k):

        nums = [str(i) for i in range(1, n + 1)]
        used = [False] * n

        count = [0]
        ans = [""]

        def backtrack(path):

            if ans[0]:
                return

            if len(path) == n:
                count[0] += 1

                if count[0] == k:
                    ans[0] = "".join(path)

                return

            for i in range(n):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])

        return ans[0]


#         backtrack([])
#         return result[k-1]

            
        
            

            
        