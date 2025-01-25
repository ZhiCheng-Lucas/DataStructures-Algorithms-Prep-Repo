# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by swapping each node's left and right children recursively.

        The process:
        1. Start at the root node
        2. For each node, swap its left and right children
        3. Recursively apply the same process to both subtrees

        Time complexity: O(n)
        Space complexity: O(n)
        """
        # Base case: if node is None (empty tree or leaf node's child)
        if not root:
            return None

        # Swap the left and right children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
