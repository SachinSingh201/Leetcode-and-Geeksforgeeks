class Solution(object):
    def combinationSum2(self, candidates, target):

        candidates.sort()
        result = []

        def dfs(index, current_sum, path):

           
            if current_sum == target:
                result.append(path[:])
                return

           
            if current_sum > target:
                return

            for i in range(index, len(candidates)):

                
                if current_sum + candidates[i] > target:
                    break

               
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                
                path.append(candidates[i])

                
                dfs(i + 1,
                    current_sum + candidates[i],
                    path)

               
                path.pop()

        dfs(0, 0, [])

        return result