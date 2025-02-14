class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Determines if cards can be arranged into groups of consecutive numbers.

        Strategy:
        1. Count frequency of each card value using a hashmap
        2. Use a min heap to process cards in ascending order
        3. For each minimum value, check if we can form a consecutive group

        Time Complexity: O(N * log N) where N is length of hand
        Space Complexity: O(N) for hashmap and heap
        """
        # If total cards can't be divided evenly into groups, return False
        if len(hand) % groupSize != 0:
            return False

        # Count frequency of each card value
        count = {}
        for card in hand:
            count[card] = count.get(card, 0) + 1

        # Create min heap from unique card values
        heap = list(count.keys())
        heapify(heap)

        while heap:
            # Get smallest card value from heap
            start_value = heap[0]

            # Try to form a group of consecutive cards
            for value in range(start_value, start_value + groupSize):
                # If any value in sequence is missing, group can't be formed
                if value not in count:
                    return False

                # Decrease count of current value
                count[value] -= 1

                # If count becomes 0, remove from heap
                # But if this value isn't the current minimum, sequence is broken
                if count[value] == 0:
                    if value != heap[0]:
                        return False
                    heappop(heap)

        return True
