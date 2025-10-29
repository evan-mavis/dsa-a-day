"""
BFS

when we reach the last iteration in the for loop for each level...
-> then we can append the node to our answer

1) right the algorithm just so I have it down
2) apply the problem 
"""

from collections import deque

class Solution:
    def rightSideView(self, root):
        ans = []

        if root == None:
            return ans 

        queue = deque([root])

        while queue:
            num_nodes_in_level = len(queue)

            last_index = num_nodes_in_level - 1

            for i in range(num_nodes_in_level):
                node = queue.popleft()

                if i == last_index:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


        