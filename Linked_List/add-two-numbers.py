# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists by first reversing them,
        converting to integers for addition, then creating a new reversed linked list.

        Time Complexity: O(N + M) where N and M are lengths of input lists
        Space Complexity: O(N + M) for storing string representations and result list

        Strategy:
        1. Reverse both input lists
        2. Convert each list to string, then to integer
        3. Add the integers
        4. Convert sum back to string and reverse it
        5. Create new linked list from reversed sum string
        """
        # Reverse first linked list
        prev = None
        while l1:
            next_node = l1.next  # Store next node
            l1.next = prev  # Reverse current node's pointer
            prev = l1  # Move prev to current node
            l1 = next_node  # Move to next node

        newl1_head = prev  # Store head of reversed first list

        # Reverse second linked list using same process
        prev = None
        while l2:
            next_node = l2.next
            l2.next = prev
            prev = l2
            l2 = next_node

        newl2_head = prev  # Store head of reversed second list

        # Convert first reversed list to string
        l1_string = ""
        while newl1_head:
            l1_string += str(newl1_head.val)
            newl1_head = newl1_head.next

        # Convert second reversed list to string
        l2_string = ""
        while newl2_head:
            l2_string += str(newl2_head.val)
            newl2_head = newl2_head.next

        # Add numbers and reverse the sum
        total_sum = int(l1_string) + int(l2_string)
        total_sum = str(total_sum)[::-1]

        # Create new linked list from reversed sum
        head = ListNode()
        result_head = head  # Store reference to head
        prev = None
        for digit in total_sum:
            head.val = int(digit)
            head.next = ListNode()
            prev = head
            head = head.next

        prev.next = None  # Remove last empty node
        return result_head
