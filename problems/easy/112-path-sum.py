class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if node == None:
                return False

            if node.left == None and node.right == None:
                return (node.val + curr) == targetSum
            
            curr += node.val    
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right

        return dfs(root, 0)
        
        
        