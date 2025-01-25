class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Cycle Detection Algorithm

        - Numbers are in range [1,n], so we can treat each value as a pointer
          to another index in the array
        - Due to the duplicate number, this creates a cycle in our "linked list"
        - Example with nums = [1,3,4,2,2]:
            0 -> nums[0] = 1
            1 -> nums[1] = 3
            3 -> nums[3] = 2
            2 -> nums[2] = 4
            4 -> nums[4] = 2 (cycle detected!)

        Mathematical Property:
        When fast and slow pointers meet at intersection point:
        - Distance from start to cycle entrance = Distance from intersection to cycle entrance

        This is because:
        Let's say:
        - Distance from start to cycle entrance = x
        - Distance from cycle entrance to intersection = y
        - Cycle length = c

        At intersection:
        - Slow pointer traveled: x + y
        - Fast pointer traveled: x + y + nc (where n is some integer)
        - We know fast travels twice the distance: 2(x + y) = x + y + nc
        - Therefore: x = nc - y
        - This means x equals the remaining distance to cycle entrance from intersection

        Time: O(n) - One pass to find intersection, one to find entrance
        Space: O(1) - Only using two pointers
        """
        # Phase 1: Find intersection point
        slow = fast = 0

        # Do while Loop
        while True:
            slow = nums[slow]  # Move one step
            fast = nums[nums[fast]]  # Move two steps
            if slow == fast:
                break

        # Phase 2: Find cycle entrance (duplicate number)
        # Moving same speed from start and intersection will meet at cycle entrance
        new_slow = 0
        while slow != new_slow:
            slow = nums[slow]
            new_slow = nums[new_slow]

        return slow
