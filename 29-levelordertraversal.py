# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        queue = deque([root])
        res = []
        levelNum = 0

        while queue: 
            levelNum = len(queue)
            temp = []
            for i in range(levelNum):
                current_node = queue.popleft()

                if current_node.left: 
                    queue.append(current_node.left)

                if current_node.right: 
                    queue.append(current_node.right)

                temp.append(current_node.val)
            res.append(temp)

        return res