# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list using recursion.
        The approach works by recursively reaching the end of the list,
        then rebuilding the links in reverse order.

        Time Complexity: O(n) - visits each node once
        Space Complexity: O(n) - recursive call stack depth
        """
        # Base case: empty list or single node
        if not head:
            return None

        # For the last node.
        # Since the last node will not enter head.next
        reversed_head = head

        # Recursively reverse the rest of the list
        if head.next:
            # Keep going until we reach the last node
            reversed_head = self.reverseList(head.next)

            # At this point, for input 1->2->3->4->5:
            # If we're at node 4, node 5 is already reversed
            # Make node 5 point back to 4: 5->4
            head.next.next = head

        # Break the original forward link
        # If we're at node 4: 4->5 becomes 4->None
        # This prevents cycles in the reversed list
        head.next = None

        return reversed_head
