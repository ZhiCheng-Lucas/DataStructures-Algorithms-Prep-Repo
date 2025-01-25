# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree contains a subtree identical to the given subRoot tree.

        Strategy:
        1. Use a helper function isSameTree to check if two trees are identical
        2. For each node in the main tree:
           - Check if the subtree rooted at current node matches subRoot
           - If not, recursively check left and right children

        Time:  O(m * n) where m is nodes in root tree, n is nodes in subRoot
        Space: O(h) where h is height of the root tree due to recursion stack
        """

        def isSameTree(tree1, tree2):
            # Base case: both nodes are None (empty trees match)
            if not tree1 and not tree2:
                return True

            # One tree is empty while other isn't (no match)
            if not tree1 or not tree2:
                return False

            # Current nodes must match and their subtrees must be identical
            if tree1.val != tree2.val:
                return False

            return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)

        # Empty subtree is always considered present
        if not subRoot:
            return True

        # Empty main tree cannot contain a non-empty subtree
        if not root:
            return False

        # Check if current root matches, if not check children
        if isSameTree(root, subRoot):
            return True

        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
