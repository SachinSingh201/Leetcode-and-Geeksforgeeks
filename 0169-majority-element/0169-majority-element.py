class Solution(object):
    def majorityElement(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = arr[0]
        count = 0 
        for num in arr:
            if num == ans:
                count+=1
            else :
                count-=1
            if count == 0:
                ans = num
                count = 1 
        return ans