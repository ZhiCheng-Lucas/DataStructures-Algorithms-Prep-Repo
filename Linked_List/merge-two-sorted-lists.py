# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists by comparing node values and linking them in ascending order.
        Uses a dummy node to handle edge cases and simplify the merging process.

        Time: O(n + m) where n and m are lengths of list1 and list2
        Space: O(1) as we only reuse existing nodes
        """
        # Create dummy node to avoid edge cases with empty lists
        dummy = ListNode()
        tail = dummy

        # Compare and link nodes while both lists have elements
        while list1 and list2:
            if list1.val >= list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        # Attach remaining nodes from non-empty list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
