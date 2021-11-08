# Problem link --> https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        Left_side = self.maxDepth(root.left)
        right_side = self.maxDepth(root.right)
        
        return max(Left_side, right_side) + 1