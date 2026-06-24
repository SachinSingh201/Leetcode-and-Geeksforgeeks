# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def countNodes(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#         if not root:
#             return 0 

#         queue = [root]
#         count = 0
#         while queue:
#             node = queue.pop(0)
#             count+=1
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         return count


class Solution:
    def countNodes(self, root):
        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        if not root:
            return 0

        lh = left_height(root)
        rh = right_height(root)

        
        if lh == rh:
            return (1 << lh) - 1

        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        