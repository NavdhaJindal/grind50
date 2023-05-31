"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = deque([node])
        clones = {node.val: Node(node.val, [])}

        while queue:
            cur_node = queue.popleft()
            
            clone = clones[cur_node.val]

            for neighbor in cur_node.neighbors:
                if neighbor.val not in clones:
                    queue.append(neighbor)
                    clones[neighbor.val] = Node(neighbor.val, [])

                clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]