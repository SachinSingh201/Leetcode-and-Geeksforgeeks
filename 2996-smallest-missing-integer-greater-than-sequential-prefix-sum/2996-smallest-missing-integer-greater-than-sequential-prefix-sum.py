# class Solution(object):
#     def missingInteger(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i = 1
#         prefix = nums[0]
#         st = set(nums)
#         while nums[i] > nums[i-1]:
#             prefix += nums[i]
#             i+=1
#         if prefix not in st:
#             return prefix
#         while prefix in st:
#                 prefix+=1
#         return prefix

class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Calculate the sum of the longest sequential prefix
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break  
        
      
        st = set(nums)
        

        while prefix_sum in st:
            prefix_sum += 1
            
        return prefix_sum

        