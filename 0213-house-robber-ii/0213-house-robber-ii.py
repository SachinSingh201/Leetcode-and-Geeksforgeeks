class Solution(object):
    def rob1(self, nums, start, end):
        prev2 = 0
        prev1 = 0

        for i in range(start, end):
            take = nums[i] + prev2
            nonTake = prev1

            curr = max(take, nonTake)

            prev2 = prev1
            prev1 = curr

        return prev1

    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        
        ans1 = self.rob1(nums, 0, n - 1)

        
        ans2 = self.rob1(nums, 1, n)

        return max(ans1, ans2)