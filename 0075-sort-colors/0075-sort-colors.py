class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z = 0 
        t = len(nums)-1
        i = 0
        while i <=t :
            if nums[i] == 2:
                nums[t],nums[i] = nums[i],nums[t]
                t-=1
            elif nums[i] == 0:
                nums[i],nums[z] = nums[z],nums[i]
                z+=1
                i+=1
            else:

                i+=1
        return nums
