class Solution(object):
    def countMajoritySubarrays(self, nums, k):
        ans = 0
        n = len(nums)
        
        for i in range(n):
            k_count = 0
            for j in range(i, n):
                if nums[j] == k:
                    k_count += 1
                
                length = j - i + 1
                if k_count > length // 2:
                    ans += 1
                    
        return ans
