"""
BFS
-> we need to do some kind of operation at each level of the tree

1) implement the bfs algo
2) implement problem specific logic
    ->
"""
from collections import deque

class Solution:
    def largestValues(self, root):
        ans = []

        if root == None:
            return ans

        queue = deque([root])
        
        while queue:
            num_nodes_in_level = len(queue)
            max_in_level = float('-inf')
            
            for _ in range(num_nodes_in_level):
                node = queue.popleft()
                
                max_in_level = max(max_in_level, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(max_in_level)

        return ans
                
                

        