# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def binaryTreePaths(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[str]
#         """
#         ans = []
#         def traversal(curr_node, path):
#             if not curr_node:
#               return 

#             path.append(str(curr_node.val))
#             if not curr_node.left and not curr_node.right:
#                 ans.append("->".join(path))  
#             traversal(curr_node.left,path)
#             traversal(curr_node.right,path)
#             path.pop()
            
#         traversal(root,[])
#         return ans
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                result.append(path)
                return

            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return result
        
        