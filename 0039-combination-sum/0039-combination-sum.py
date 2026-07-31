class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def dfs(index, target, path):
            # Target achieve ho gaya
            if target == 0:
                result.append(path[:])
                return

            # Invalid case
            if target < 0 or index == len(candidates):
                return

            # Choice 1: Current element lo
            path.append(candidates[index])
            dfs(index, target - candidates[index], path)
            path.pop()

            # Choice 2: Current element skip karo
            dfs(index + 1, target, path)

        dfs(0, target, [])
        return result