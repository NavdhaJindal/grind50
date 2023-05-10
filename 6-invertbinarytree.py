class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root