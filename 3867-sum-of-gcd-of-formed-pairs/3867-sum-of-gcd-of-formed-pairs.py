import math

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        preGcd = [0] * n
        maxVal = 0
        
        for i in range(n):
            if nums[i] > maxVal:
                maxVal = nums[i]
            preGcd[i] = math.gcd(nums[i], maxVal)
            
        preGcd.sort()
        
        total_sum = 0
        l, r = 0, n - 1
        
        while l < r:
            total_sum += math.gcd(preGcd[l], preGcd[r])
            l += 1
            r -= 1
            
        return total_sum