class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find the kth largest element using a max heap approach.

        Strategy:
        1. Convert the array into a max heap by negating all elements
           (Python only provides min heap, so we negate to simulate max heap)
        2. Pop k-1 largest elements from the heap
        3. The top of remaining heap is our kth largest element

        Time Complexity: O(n + k log n)
        - O(n) to build the heap
        - O(k log n) for k heap operations

        Space Complexity: O(n)
        - We store all elements in the heap
        """
        # Convert to max heap by negating all elements
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        # Remove k-1 largest elements
        for _ in range(k - 1):
            heapq.heappop(max_heap)

        # Return kth largest (don't forget to negate back)
        return -max_heap[0]
