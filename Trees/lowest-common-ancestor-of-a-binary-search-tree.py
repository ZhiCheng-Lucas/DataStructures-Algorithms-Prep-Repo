# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        Find the lowest common ancestor of two nodes in a Binary Search Tree.
        Takes advantage of BST properties where left subtree contains smaller values
        and right subtree contains larger values than the current node.

        Key properties:
        - All node values are unique
        - p and q are guaranteed to exist in the tree
        - p and q are distinct nodes

        Time complexity: O(h) , where h is the height of the tree
        Space complexity: O(h)
        """
        # If current node is either p or q, it is the LCA
        if root == p or root == q:
            return root

        # Order p and q by their values for easier comparison
        max_node = p if p.val > q.val else q
        min_node = q if p.val > q.val else p

        # Current node's value is between p and q, making it their LCA
        if root.val > min_node.val and root.val < max_node.val:
            return root

        # If root is greater than both nodes, LCA must be in left subtree
        elif root.val > max_node.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If root is smaller than both nodes, LCA must be in right subtree
        else:
            return self.lowestCommonAncestor(root.right, p, q)
