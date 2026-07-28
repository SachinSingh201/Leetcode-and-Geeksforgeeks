# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]

        """
        inorder_map = {val:idx for idx,val in enumerate(inorder)}
        self.postIdx = -1
        def helper(left,right):
            if left > right:
                return
            rootVal = postorder[self.postIdx]
            self.postIdx -=1
            root = TreeNode(rootVal)
            pivotIdx = inorder_map[rootVal]
            root.right = helper(pivotIdx+1,right)
            root.left = helper(left,pivotIdx-1)

            return root
        return helper(0,len(inorder)-1)

        