class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        stack = [root]
        while (stack):
            current_node = stack.pop()
            if current_node:
                temp = current_node.left
                current_node.left = current_node.right
                current_node.right = temp
                stack.extend([current_node.left, current_node.right])

        return root
        # if root == None:
        #     return None
        # temp = root.right
        # root.right = root.left
        # root.left = temp
        # self.invertTree(root.right)
        # self.invertTree(root.left)
        # return root