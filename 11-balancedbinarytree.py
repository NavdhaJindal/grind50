class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root: 
            return True
        return (abs(height(root.left) - height(root.right)) < 2)