class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # hashmap = {}
        # for i in range(1,n+2):
        #     hashmap[i] = False
        
        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] = True
        # ans = -1
        # for key , value in hashmap.items():
        #     if value == False:
        #         ans = key 
        #         break 
        # return ans
        i = 0
        while i < n:
            correct = nums[i]- 1

            if 1 <= nums[i] <= n and nums[i]!= nums[correct]:
                nums[i], nums[correct] = nums[correct],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!= i+1:
                return i+1
        return n+1

        