class KthLargest:
    """
    Maintains a stream of test scores and returns the kth highest score in real-time.
    Uses a min-heap of size k to efficiently track the k largest elements.

    The min-heap approach is optimal because:
    1. We only need to maintain k elements
    2. The smallest of these k elements (root of min-heap) is our kth largest
    3. New elements can be processed in O(log k) time

    Time Complexity:
        - Initialization: O(n log k) where n is length of initial array
        - Add operation: O(log k)
    Space Complexity: O(k) to store the k largest elements
    """

    def __init__(self, k: int, nums: List[int]):
        # Initialize min-heap with input array and keep track of k
        self.heap = nums
        self.k = k

        # Convert input array to min-heap in O(n) time
        heapq.heapify(self.heap)

        # Remove smaller elements until heap size is k
        # This ensures heap only contains k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add new score to heap
        heapq.heappush(self.heap, val)

        # If heap exceeds k elements, remove smallest
        # This maintains our invariant of keeping k largest elements
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Root of min-heap is kth largest element
        return self.heap[0]
