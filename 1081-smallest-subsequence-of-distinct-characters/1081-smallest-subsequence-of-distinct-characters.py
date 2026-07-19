class Solution(object):
    def smallestSubsequence(self, s):
        vis = [0] * 26
        num = [0] * 26

        for ch in s:
            num[ord(ch) - ord('a')] += 1

        stk = []

        for ch in s:
            idx = ord(ch) - ord('a')

           
            num[idx] -= 1

           
            if vis[idx]:
                continue

            while stk and stk[-1] > ch:
                topIdx = ord(stk[-1]) - ord('a')

                if num[topIdx] == 0:
                    break

                vis[topIdx] = 0
                stk.pop()

            stk.append(ch)
            vis[idx] = 1

        return "".join(stk)