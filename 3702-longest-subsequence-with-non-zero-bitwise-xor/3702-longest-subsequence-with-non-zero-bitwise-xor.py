class Solution(object):
    def longestSubsequence(self, nums):
        completeXor = 0

        for num in nums:
            completeXor ^= num

        if completeXor != 0:
            return len(nums)

        for num in nums:
            if num != 0:
                return len(nums) - 1

        return 0