# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Uses Floyd's Cycle Finding Algorithm (Tortoise and Hare)

        The algorithm uses two pointers moving at different speeds:
        - Fast pointer moves 2 steps
        - Slow pointer moves 1 step

        If a cycle exists, the pointers will meet since the fast pointer
        will eventually "lap" the slow pointer within the cycle.
        If no cycle, fast pointer reaches end of list.

        Time: O(n) - traverses list once
        Space: O(1) - only uses two pointers
        """
        if not head:
            return False

        tortoise = head
        hare = head

        while hare and hare.next:
            hare = hare.next.next  # Move 2 steps
            tortoise = tortoise.next  # Move 1 step

            if hare == tortoise:  # Cycle detected
                return True

        return False  # Hare reached end, no cycle
