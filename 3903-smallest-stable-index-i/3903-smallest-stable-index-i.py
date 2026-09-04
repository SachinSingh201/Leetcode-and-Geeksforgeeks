class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        if nums[0] - suffix_min[0] <= k:
            return 0

        prefix_max = nums[0]

       
        for i in range(1, n):
            
            if prefix_max - suffix_min[i] <= k:
                return i

            prefix_max = max(prefix_max, nums[i])

        return -1