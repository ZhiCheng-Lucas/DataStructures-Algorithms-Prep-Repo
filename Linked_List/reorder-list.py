# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Solution Approach:
        The problem requires reordering a linked list by alternating between nodes from the beginning
        and end. This can be solved in three steps:

        1. Split the list into two halves using the slow/fast pointer technique
        2. Reverse the second half
        3. Merge the first half with the reversed second half

        Examples:
        [1,2,3,4] becomes [1,4,2,3]
        - Split into [1,2] and [3,4]
        - Reverse second half to get [1,2] and [4,3]
        - Merge alternately

        [1,2,3,4,5] becomes [1,5,2,4,3]
        - Split into [1,2,3] and [4,5]
        - Reverse second half to get [1,2,3] and [5,4]
        - Merge alternately

        Time: O(n) - one pass for each step
        Space: O(1) - only pointer manipulation
        """
        if not head or not head.next:
            return

        # Step 1: Split the list into two halves
        # Use slow/fast pointers to find the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # At this point:
        # - slow points to the last node of first half
        # - slow.next is the start of second half
        second_half = slow.next
        slow.next = None  # Terminate first half

        # Step 2: Reverse the second half
        # Use three pointers to reverse links
        prev = None
        curr = second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # prev is now the head of reversed second half
        second_half = prev

        # Step 3: Merge both halves alternately
        # Save next pointers before changing links
        first = head
        while second_half:
            first_next = first.next
            second_next = second_half.next

            first.next = second_half
            second_half.next = first_next

            first = first_next
            second_half = second_next
