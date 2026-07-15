class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count =0
        hashmap = {0:1}
        for num in nums:
            prefix_sum += num
            if (prefix_sum-k) in hashmap:
                count+= hashmap[prefix_sum-k]

            hashmap[prefix_sum] = hashmap.get(prefix_sum,0) +1
        return count     





        