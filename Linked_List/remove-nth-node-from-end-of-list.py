# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two-pointer approach to remove the nth node from end:

        Strategy:
        1. Create a dummy node to handle edge cases (like removing first element)
        2. Use two pointers (left and right) separated by n nodes
        3. When right reaches end, left will be at the node before target

        Example for n=2:
        Initial:    dummy -> 1 -> 2 -> 3 -> 4 -> 5
                     L         R
        After gap:   dummy -> 1 -> 2 -> 3 -> 4 -> 5
                     L              R
        Final:       dummy -> 1 -> 2 -> 3 -> 4 -> 5
                                    L              R

        Time: O(n) - one pass through the list
        Space: O(1) - only using pointers
        """
        dummy_node = ListNode(0, head)  # Dummy node helps handle edge cases
        left = dummy_node  # Points to node before the one to be removed
        right = head  # Will be used to maintain n-gap from left

        # Create n-gap between right and left pointers
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until right reaches end
        while right:
            right = right.next
            left = left.next

        # Remove the nth node by updating next pointer
        left.next = left.next.next

        return dummy_node.next
