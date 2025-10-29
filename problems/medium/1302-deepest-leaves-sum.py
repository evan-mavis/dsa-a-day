"""
BFS
-> I can just keep calculating the sum of each row
each row sum will override the last

then return the last row

1) implement the BFS also
2) apply the specific problem logic
"""
from collections import deque

class Solution:
    def deepestLeavesSum(self, root):
        if root is None:
            return 0 

        queue = deque([root])

        while queue:
            curr_sum = 0
            num_nodes_in_level = len(queue)

            for _ in range(num_nodes_in_level):
                node = queue.popleft()

                curr_sum += node.val
                
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
        
        return curr_sum
