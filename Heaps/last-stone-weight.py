# Time complexity: O(nlogn)
# Space complexity: O(n)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max heap by negating values since Python only has min heap
        # This allows us to easily get the two heaviest stones each time
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # Continue until we have 0 or 1 stone left
        while len(max_heap) > 1:
            # Get the two heaviest stones (need to negate to get actual weights)
            stone1 = -heapq.heappop(max_heap)  # Heaviest stone
            stone2 = -heapq.heappop(max_heap)  # Second heaviest stone

            # If stones have different weights, put remaining weight back
            # Weight = difference between the stones
            if stone1 != stone2:
                remaining_weight = stone1 - stone2
                heapq.heappush(max_heap, -remaining_weight)
            # If stones are equal, both are destroyed (no need to push back)

        # Return the last stone's weight if exists, otherwise 0
        return -max_heap[0] if max_heap else 0
