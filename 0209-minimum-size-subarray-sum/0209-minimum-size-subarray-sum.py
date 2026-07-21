class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)

        i = 0
        curr_sum = 0
        ans = float('inf')

        for j in range(n):

        
            curr_sum += nums[j]

        
            while curr_sum >= target:

                ans = min(ans, j - i + 1)

                curr_sum -= nums[i]
                i += 1

        return 0 if ans == float('inf') else ans