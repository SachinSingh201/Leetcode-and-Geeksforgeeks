class Solution(object):
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        ans = []

        for i in range(len(target)):
            x = ord(target[i]) - 97

            if cnt[x]:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                break
        else:
            
            i = len(target) - 1

        while i >= 0:

            if i < len(ans):
                cnt[ord(ans[i]) - 97] += 1
                ans.pop()

            x = ord(target[i]) - 97

           
            for c in range(x + 1, 26):
                if cnt[c]:
                    cnt[c] -= 1

                    result = ans + [chr(c + 97)]

                    
                    for k in range(26):
                        result.extend([chr(k + 97)] * cnt[k])

                    return ''.join(result)

            i -= 1

        return ""