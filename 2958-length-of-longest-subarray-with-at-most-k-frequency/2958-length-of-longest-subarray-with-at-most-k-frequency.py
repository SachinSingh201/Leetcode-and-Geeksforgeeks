from collections import Counter

class Solution(object):

    def maxSubarrayLength(self, nums, k):

        ans = 0
        start = -1
        frequency = Counter()

        for end in range(len(nums)):

            frequency[nums[end]] += 1

            while frequency[nums[end]] > k:
                start += 1
                frequency[nums[start]] -= 1

            ans = max(ans, end - start)

        return ans