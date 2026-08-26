class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        cnt = 0
        ans = ""
        for j in range(len(s)):
            if s[j] == "1":
                cnt+=1
            while cnt == k:
                current = s[i:j+1]
                if (ans == "" or len(current) < len(ans) or (len(current) == len(ans) and current < ans)):
                    ans = current
                if s[i] == "1":
                    cnt -=1
                i+=1
        return ans
            


        

        


        