# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def max_height(node) -> int:
            nonlocal max_length
            right_height = 0
            left_height = 0
            
            if not node: 
                return 0

            if not (node.right or node.left):
                return 0

            if node.right:
                right_height = max_height(node.right) + 1

            if node.left:
                left_height = max_height(node.left) + 1

            max_length = max(max_length, right_height + left_height)
            return max(right_height, left_height)

        max_height(root)
        return max_length