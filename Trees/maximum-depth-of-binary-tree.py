# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Finds the maximum depth of a binary tree using recursive DFS.

        For each node:
        1. If node is None, depth is 0
        2. Otherwise, depth is 1 (current node) + max depth between left and right subtrees

        Time: O(n)
        Space: O(n)
        """

        # Base case: empty tree has depth 0
        if not root:
            return 0

        # Recursive case: depth is 1 (current node) + max depth of subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
