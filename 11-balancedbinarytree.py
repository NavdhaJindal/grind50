class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def height(root):
            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            if left_height == -1 or right_height == -1:
                return -1

            if (abs(right_height - left_height) > 1):
                return -1
            
            return max(height(root.left), height(root.right)) + 1

        if not root: 
            return True
        if height(root) == -1: 
            return False
        else: 
            return True

        # def height(root):
        #     if not root:
        #         return 0
        #     return max(height(root.left), height(root.right)) + 1

        # if not root: 
        #     return True
        # return (abs(height(root.left) - height(root.right)) < 2)

        #this solution only checks for height of the top 2 children of the root node. It doesn't check if the children have unbalanced children