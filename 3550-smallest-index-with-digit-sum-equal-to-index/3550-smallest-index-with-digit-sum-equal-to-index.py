class Solution(object):
    def smallestIndex(self, nums):
        def digitSum(num):
            ans = 0
            while num > 0:
                digit = num % 10 
                ans += digit
                num = num //10
            return ans
        for  i in range(len(nums)):
            dSum = digitSum(nums[i])
            if i == dSum :
                return i 
        return -1

        