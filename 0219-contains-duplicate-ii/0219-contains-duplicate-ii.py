class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
       
        ans = False 
        seen = {}
        for idx , val in enumerate(nums):
            if val not  in seen :
                seen[val] = idx
            else:
                j = seen.get(val)
                if abs(idx-j) <= k:
                    ans = True
                else:
                    seen[val] = idx
                                   
        return ans