class Solution(object):
    def removeDuplicates(self, nums):
        
        currVal = -1
        prevVal = nums[0]
        i = 1
        k = 1
        
        while k < len(nums):
            currVal = nums[k]
            
            if currVal == prevVal:
                pass
                
            else:
                prevVal = currVal
                nums[i] = currVal
                i += 1
                
            k += 1
        
        return i