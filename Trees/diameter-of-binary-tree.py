# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the diameter of a binary tree, which is the longest path between any two nodes.

        - For each node, the potential diameter passing through it is the sum of:
          left subtree height + right subtree height
        - The longest diameter might not pass through the root
        - We need to track the maximum diameter seen across all nodes

        Time Complexity: O(n) - Visit each node once
        Space Complexity: O(h) - Recursion stack depth equals tree height
        """
        # Track the maximum diameter found so far
        self.max_diameter = 0

        def getHeight(node):
            # Base case: empty node has height 0
            if not node:
                return 0

            # Get heights of left and right subtrees
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)

            # Diameter through current node = left height + right height
            # Update max_diameter if current path is longer
            self.max_diameter = max(left_height + right_height, self.max_diameter)

            # Return height of current node's subtree
            # Height = max of left/right subtree + 1 (current node)
            return max(left_height, right_height) + 1

        getHeight(root)
        return self.max_diameter
