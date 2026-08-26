class Solution(object):
    def lowerbound(self,nums,target):
        n = len(nums)
        l = 0
        r = n-1
        ans = n
        while l<=r:
            mid = (l+r) //2
            if nums[mid] >= target:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans



    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lis = []
        lis.append(nums[0])
        for i in range(1,n):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                lb = self.lowerbound(lis,nums[i])
                lis[lb] = nums[i]
        return len(lis)

        