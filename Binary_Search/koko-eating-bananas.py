class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Find the minimum eating speed needed to consume all bananas.

        Approach:
        Uses binary search to efficiently find the minimum speed:
        1. The minimum possible speed is 1 banana per hour
        2. The maximum needed speed is max(piles), as eating faster wouldn't help
        3. For each tested speed, we check if all piles can be eaten within h hours

        Time Complexity: O(n * log m) where n = len(piles), m = max(piles)
        Space Complexity: O(1)
        """
        min_k = 1
        max_k = max(piles)
        best_speed = max_k  # Stores the minimal valid speed found so far

        while min_k <= max_k:
            test_speed = (min_k + max_k) // 2

            # Calculate total hours needed at current speed
            hours_needed = 0
            for pile in piles:
                hours_needed += ceil(pile / test_speed)

            if hours_needed <= h:
                # Current speed works - try finding a slower valid speed
                best_speed = min(best_speed, test_speed)
                max_k = test_speed - 1
            else:
                # Too slow - need to eat faster
                min_k = test_speed + 1

        return best_speed
