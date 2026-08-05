# class Solution(object):
#     def pathSum(self, root, targetSum):

#         if not root:
#             return 0

#         # Count paths starting from current node
#         def dfs(node, target):
#             if not node:
#                 return 0

#             count = 0

#             if node.val == target:
#                 count += 1

#             count += dfs(node.left, target - node.val)
#             count += dfs(node.right, target - node.val)

#             return count

#         return (
#             dfs(root, targetSum)
#             + self.pathSum(root.left, targetSum)
#             + self.pathSum(root.right, targetSum)
#         )



class Solution(object):
    def pathSum(self, root, targetSum):

        prefix = {0: 1}

        def dfs(node, currSum):
            if not node:
                return 0

            currSum += node.val

            count = prefix.get(currSum - targetSum, 0)

            prefix[currSum] = prefix.get(currSum, 0) + 1

            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)

            prefix[currSum] -= 1

            return count

        return dfs(root, 0)