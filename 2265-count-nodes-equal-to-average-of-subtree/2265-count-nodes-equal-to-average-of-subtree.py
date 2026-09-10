# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if not node:
                return 0,0
            leftSum , leftCount = dfs(node.left)
            rightSum , rightCount = dfs(node.right)

            subTreeSum = leftSum+rightSum+node.val
            Tnodes = rightCount+leftCount+1

            if subTreeSum//Tnodes == node.val:
                self.ans+=1
            
            return subTreeSum,Tnodes
        dfs(root)
        return self.ans

    
        