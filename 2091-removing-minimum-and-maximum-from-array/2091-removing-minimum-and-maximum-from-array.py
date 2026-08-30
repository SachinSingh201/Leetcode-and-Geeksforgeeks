class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
       
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)
        
       
        delete_from_left = j + 1
        
       
        delete_from_right = n - i
        
       
        delete_from_both = (i + 1) + (n - j)
        
        
        return min(delete_from_left, delete_from_right, delete_from_both)
