"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        Deep copy a linked list with random pointers

        Strategy:
        1. Create a mapping between original nodes and their copies
        2. First pass: Create new nodes and establish the mapping
        3. Second pass: Set up random pointers using the mapping

        Time Complexity: O(n) - Two passes through the list
        Space Complexity: O(n) - HashMap storing n node mappings
        """
        # Handle empty list case
        if not head:
            return None

        # Dictionary to map original nodes to their copies
        originalToCopy = {}

        # Keep reference to the original head for second pass
        currentOriginal = head

        # Create first node of the copy
        copyHead = Node(head.val)
        copyTail = copyHead  # Track the last valid node

        # First pass: Create copies and build next pointers
        while currentOriginal:
            # Map current original node to its copy
            originalToCopy[currentOriginal] = copyTail

            # Create next node if not at the end
            if currentOriginal.next:
                copyTail.next = Node(currentOriginal.next.val)
                copyTail = copyTail.next

            currentOriginal = currentOriginal.next

        # Second pass: Set up random pointers
        currentOriginal = head
        while currentOriginal:
            copyNode = originalToCopy[currentOriginal]
            # Map random pointer using the originalToCopy dictionary
            copyNode.random = originalToCopy.get(currentOriginal.random)
            currentOriginal = currentOriginal.next

        return copyHead
