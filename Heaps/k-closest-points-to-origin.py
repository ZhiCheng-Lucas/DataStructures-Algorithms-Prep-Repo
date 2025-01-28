class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Find the k closest points to origin (0,0) using a min heap approach.

        Strategy:
        1. Build a min heap of points, ordered by their distance from origin
        2. Extract k closest points from the heap

        Time Complexity: O(n + k*log n)
        - O(n) to build the heap (heapify)
        - O(k*log n) to extract k elements from heap

        Space Complexity: O(n) for the heap

        Note: We can skip the square root calculation since comparing squared
        distances maintains the same ordering as actual distances

        This is faster than sorting a distance array since sorting is nlogn.
        """
        # Store (squared_distance, x, y) tuples in min heap
        min_heap = []
        for x, y in points:
            squared_dist = x * x + y * y  # Avoid sqrt for efficiency
            min_heap.append((squared_dist, x, y))

        # Convert list to min heap in O(n)
        heapq.heapify(min_heap)

        # Extract k closest points
        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            result.append([x, y])

        return result
