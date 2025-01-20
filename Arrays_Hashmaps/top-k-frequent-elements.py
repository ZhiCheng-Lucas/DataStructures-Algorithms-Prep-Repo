class Solution:
    """
    Find k most frequent elements using bucket sort for linear time complexity.

    Solution approach:
    Uses bucket sort where bucket index represents frequency:
    1. Count element frequencies using a hashmap
    2. Create buckets where index = frequency
    3. Place elements in corresponding frequency buckets
    4. Walk buckets from highest to lowest frequency

    Visual example for nums = [1,1,1,2,2,3], k = 2:
    1. frequency map = {1:3, 2:2, 3:1}
    2. buckets array = [
         [],    # frequency 0 (unused)
         [3],   # elements occurring once
         [2],   # elements occurring twice
         [1]    # elements occurring thrice
       ]
    3. result = [1, 2]  # walking from index 3 down

    Time Complexity: O(n) - linear scan and bucket sort
    Space Complexity: O(n) - for frequency map and buckets
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create frequency map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Create and populate frequency buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Collect top k elements from highest frequency buckets
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
