class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        partition = len(s)//2
        # bucket = [0]*26

        # for i in range(partition):
        #     bucket[ord(s[i]) - 97] += 1
        # left = "".join([chr(i+97) * bucket[i] for i in range(26)  if bucket[i] > 0])
        left =sorted(s[:partition])
    

        mid = [s[partition]] if len(s)%2 != 0 else []
        right = left[::-1]
        return "".join(left+mid+right)
        