# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        A recursive approach to compare two binary trees node by node.
        The trees are identical if:
        1. Both nodes are None (empty)
        2. Both nodes have same value
        3. Their left and right subtrees are identical

        Time Complexity: O(min(n,m)) where n,m are the sizes of trees p and q
        Space Complexity: O(min(h1,h2)) where h1,h2 are the heights of the trees
                         due to recursive call stack
        """
        # If both nodes are None, trees are identical
        if p == None and q == None:
            return True

        # If only one node is None, trees are different
        if p == None or q == None:
            return False

        # Compare current node values
        if p.val != q.val:
            return False

        # Recursively check left and right subtrees
        # Both subtrees must be identical for trees to be same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
