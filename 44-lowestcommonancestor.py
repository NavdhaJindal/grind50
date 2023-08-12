# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root

        right = self.lowestCommonAncestor(root.right, p, q)
        left = self.lowestCommonAncestor(root.left, p, q)

        if right and left: 
            return root

        else: 
            return right or left

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         def findNode(root: 'TreeNode', node: 'TreeNode') -> List['TreeNode']:
#             if not root: 
#                 return []
#             if root == node: 
#                 return [root]
#             backtrack = findNode(root.right, node)
#             if backtrack: 
#                 backtrack.append(root)
#                 return backtrack
#             else: 
#                 backtrack = findNode(root.left, node)
#                 if backtrack:
#                     backtrack.append(root)
#                     return backtrack
#                 else: 
#                     return []

#         q_path = findNode(root, q)
#         p_path = findNode(root, p)

#         lca = root
#         while q_path and p_path: 
#             p_parent, q_parent = p_path.pop(), q_path.pop()
#             if p_parent == q_parent: 
#                 lca = p_parent
#             else: 
#                 break
        
#         return lca