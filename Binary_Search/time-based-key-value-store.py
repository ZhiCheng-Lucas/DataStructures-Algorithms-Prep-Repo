class TimeMap:
    """
    A time-based key-value store that supports retrieving values based on timestamps.

    The data structure uses a hashmap where:
    - Key: string identifier
    - Value: list of [timestamp, value] pairs, sorted by timestamp (guaranteed by problem constraints)

    Time Complexity:
    - Set: O(1) - Appending to list
    - Get: O(n) for linear search, where n is number of values for a key
          O(log n) for binary search implementation

    Space Complexity: O(n) where n is total number of key-value pairs stored
    """

    def __init__(self):
        # Store key-value pairs with timestamps: {key: [[timestamp1, value1], [timestamp2, value2], ...]}
        self.time_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Create empty list for new keys or append to existing key's list
        if key not in self.time_store:
            self.time_store[key] = []
        self.time_store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # Linear Search Implementation - O(n)
        # Search from latest timestamp since we're looking for the most recent valid value
        if key in self.time_store:
            values = self.time_store[key]
            for i in range(len(values) - 1, -1, -1):
                if values[i][0] <= timestamp:
                    return values[i][1]
        return ""

        # Binary Search Implementation - O(log n)
        # Note: While theoretically faster with O(log n) vs O(n), this implementation
        # performed slower in practice. I assume this is due to small dataset sizes
        # in the test cases, as binary search overhead might outweigh its benefits
        # for small n. For larger datasets, this implementation should be more efficient.

        """
        result = ""
        if key in self.time_store:
            values = self.time_store[key]
            left, right = 0, len(values) - 1
            
            while left <= right:
                mid = (left + right) // 2
                curr_timestamp = values[mid][0]

                if curr_timestamp == timestamp:
                    return values[mid][1]
                
                if curr_timestamp < timestamp:
                    # Store the current value as potential result and look for a closer timestamp
                    result = values[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1

        return result
        """
