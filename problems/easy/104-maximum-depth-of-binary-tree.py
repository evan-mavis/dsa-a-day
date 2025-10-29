"""
DFS algo
1. base case
2. left child
3. right child
4. return 
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0

            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            
            return max(left, right)  

        return dfs(root)
        
""" 
      1
    /   \ 
   2     3
        / \ 
       4   5
"""
