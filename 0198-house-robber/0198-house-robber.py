class Solution(object):
   
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if  n ==1:
            return nums[0]
        a = nums[0]
        b = max(nums[0],nums[1])

        for i in range(2,n):
            take = a+nums[i]
            not_take = b 
            c = max(take,not_take)

            a = b
            b = c
        return b
