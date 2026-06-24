# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.global_max = float('-inf')
        
        def gain_from_subtree(node):
            if not node:
                return 0

            left_gain = max(gain_from_subtree(node.left), 0)
            right_gain = max(gain_from_subtree(node.right), 0)
            
            
            current_path_sum = node.val + left_gain + right_gain
            
            
            self.global_max = max(self.global_max, current_path_sum)
            
           
            return node.val + max(left_gain, right_gain)
        
        gain_from_subtree(root)
        return self.global_max
