class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0 

            if root.left is None and root.right is None:
                return 1

            return 1 + min(dfs(root.left), dfs(root.right))

        return dfs(root)

"""
             1
        2        3
    4      5        
"""
