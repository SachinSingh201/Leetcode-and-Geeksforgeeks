class Solution(object):
    def minimumPushes(self, word):

        hashmap = {}

        for ch in word:
            hashmap[ch] = hashmap.get(ch, 0) + 1

        freq = sorted(hashmap.values(), reverse=True)

        ans = 0

        for i, f in enumerate(freq):
            if i < 8:
                ans += f
            elif i < 16:
                ans += f * 2
            elif i < 24:
                ans += f * 3
            else:
                ans += f * 4

        return ans