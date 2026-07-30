class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = 0
        if len(word) < 9:
            ans = len(word)
        elif len(word) > 8 and len(word) < 17:
            ans = ((len(word) - 8)*2) + 8
        elif len(word)> 16 and len(word) < 25:
            ans = ((len(word) - 16)*3) + 24
        else:
            ans = ((len(word) - 24)*4) + 48

        return ans

        