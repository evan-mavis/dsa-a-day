class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        max_diameter = 0  # Track max found anywhere
        
        def dfs(root):
            nonlocal max_diameter
            
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Check diameter at every node
            max_diameter = max(max_diameter, left + right)
            
            return 1 + max(left, right)
    
        dfs(root)  # One call to populate max_diameter
        return max_diameter