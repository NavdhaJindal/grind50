class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        smaller = min(p, q, key = lambda x: x.val)
        larger = max(p, q, key = lambda x: x.val)
#use the fact that they're binary search trees

        def lca(root, s, l):
            if root:
                if (s.val <= root.val and l.val >= root.val):
                    return root
                elif s.val <= root.val and l.val <= root.val:
                    return self.lowestCommonAncestor(root.left, s, l)
                else:
                    return self.lowestCommonAncestor(root.right, s, l)
            return root

        return lca(root, smaller, larger)