# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced (the heights of the two subtrees
        of every node never differ by more than one).

        Strategy:
        - Use DFS (Depth-First Search) to check each node recursively
        - For each node, track both its height and balance status
        - A node is balanced if:
            1. Both left and right subtrees are balanced
            2. Height difference between left and right subtrees is at most 1

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        """
        if not root:
            return True

        def dfs(root):
            # Base case: empty node has height 0 and is balanced
            if not root:
                return [0, True]

            # Get height and balance status of left and right subtrees
            left_status = dfs(root.left)
            right_status = dfs(root.right)

            # If either subtree is unbalanced, current tree is unbalanced
            if not left_status[1] or not right_status[1]:
                return [0, False]

            # Check height difference between subtrees
            height_diff = abs(left_status[0] - right_status[0])
            is_balanced = height_diff <= 1

            # Current height is max of subtree heights plus 1
            current_height = max(left_status[0], right_status[0]) + 1

            return [current_height, is_balanced]

        return dfs(root)[1]
