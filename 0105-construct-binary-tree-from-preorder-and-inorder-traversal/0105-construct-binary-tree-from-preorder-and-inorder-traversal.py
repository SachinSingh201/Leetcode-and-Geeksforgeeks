# # class Solution(object):
# #     def buildTree(self, preorder, inorder):

# #         inorder_map = {}
# #         for i, val in enumerate(inorder):
# #             inorder_map[val] = i

# #         preIdx = [0]

# #         def tree(left, right):

# #             if left > right:
# #                 return None

# #             root_val = preorder[preIdx[0]]
# #             preIdx[0] += 1

# #             root = TreeNode(root_val)

# #             mid = inorder_map[root_val]

# #             root.left = tree(left, mid - 1)
# #             root.right = tree(mid + 1, right)

# #             return root

# #         return tree(0, len(inorder) - 1)



# class Solution(object):
#     def buildTree(self, preorder, inorder):

#         preIdx = [0]

#         def search(inorder, val, left, right):
#             for i in range(left, right + 1):
#                 if inorder[i] == val:
#                     return i

#         def tree(preorder, inorder, left, right):

#             if left > right:
#                 return None

#             rootVal = preorder[preIdx[0]]
#             preIdx[0] += 1

#             node = TreeNode(rootVal)

#             mid = search(inorder, rootVal, left, right)

#             node.left = tree(preorder, inorder, left, mid - 1)
#             node.right = tree(preorder, inorder, mid + 1, right)

#             return node

#         return tree(preorder, inorder, 0, len(inorder) - 1)


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left_in, right_in):
            if left_in > right_in:
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            pivot = inorder_map[root_val]
            root.left = helper(left_in, pivot - 1)
            root.right = helper(pivot + 1, right_in)
            
            return root
            
        return helper(0, len(inorder) - 1)