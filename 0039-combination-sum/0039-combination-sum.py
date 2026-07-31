class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()

        result = []
        dp = set()         

        def dfs(index, target, path):

           
            if target == 0:
                result.append(path[:])
                return True

           
            if target < 0 or index == len(candidates):
                return False

            
            if (index, target) in dp:
                return False

            found = False

            for i in range(index, len(candidates)):

                # Since array is sorted
                if candidates[i] > target:
                    break

                path.append(candidates[i])

                if dfs(i, target - candidates[i], path):
                    found = True

                path.pop()

           
            if not found:
                dp.add((index, target))

            return found

        dfs(0, target, [])
        return result