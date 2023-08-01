# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkRight(root: Optional[TreeNode]) -> bool:
            if root.right: 
                if root.right.val <= root.val:
                    return False
                else: 
                    return True
            return True

        def checkLeft(root: Optional[TreeNode]) -> bool: 
            if root.left: 
                if root.left.val >= root.val:
                    return False
                else: 
                    return True
            return True

        if not root: 
            return True
        if not (checkRight(root) and checkLeft(root)):
            return False
        return (self.isValidBST(root.right) and self.isValidBST(root.left))