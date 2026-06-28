# # class Solution(object):
# #     def findTargetSumWays(self, nums, target):
# #         """
# #         :type nums: List[int]
# #         :type target: int
# #         :rtype: int
# #         """
# #         self.ans = 0

# #         def dfs(idx,currSum):
            
# #             if idx == len(nums):
# #                 if currSum == target:
# #                     self.ans += 1
# #                 return 
            
# #             dfs(idx+1,currSum+nums[idx])
# #             dfs(idx+1,currSum-nums[idx])

# #         dfs(0,0)
# #         return self.ans


# class Solution(object):
#     def findTargetSumWays(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         memo = {}

#         def dfs(idx,currSum):
            
#             if idx == len(nums):
#                 if currSum == target:
#                     return 1
#                 else:
#                     return 0 
#             if (idx,currSum) in memo:
#                 return memo[idx,currSum]
                
                
            
#             add = dfs(idx+1,currSum+nums[idx])
#             subtract = dfs(idx+1,currSum-nums[idx])
#             memo[(idx,currSum )] = add+subtract

#             return memo[(idx,currSum)]
#         return dfs(0,0)

#         dfs(0,0)
#         return self.ans


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        total = sum(nums)
        if abs(target) > total:
            return 0

        if (target + total) % 2:
            return 0

        subset = (target + total) // 2
        dp = [0] * (subset + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset, num - 1, -1):
                dp[s] += dp[s - num]
                
        return dp[subset]
        