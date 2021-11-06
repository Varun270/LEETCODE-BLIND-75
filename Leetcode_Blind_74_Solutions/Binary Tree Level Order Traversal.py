# Problem Link --> https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        q = collections.deque()
        
        q.append(root)
        
        while q:
            q_len = len(q)
            level = []
            
            for i in range(q_len):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                ans.append(level)
                    
        return ans