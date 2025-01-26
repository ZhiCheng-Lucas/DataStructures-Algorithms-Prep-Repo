# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level-order traversal of a binary tree using BFS approach.

        The algorithm uses a queue to process nodes level by level:
        1. Start with the root node in the queue
        2. For each level:
           - Process all nodes currently in queue (these form one level)
           - Add their children to queue for next level processing
        3. Continue until queue is empty (all levels processed)

        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(n)
        """
        if not root:
            return []

        queue = deque([root])  # Initialize queue with root node
        level_order_result = []  # Store final level-by-level result

        while queue:
            current_level_size = len(queue)
            current_level = []  # Store nodes at current level

            # Process all nodes at current level
            for _ in range(current_level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)

                # Add children to queue for next level processing
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            level_order_result.append(current_level)

        return level_order_result
