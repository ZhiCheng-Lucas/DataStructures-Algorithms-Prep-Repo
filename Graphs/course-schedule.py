class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Course Schedule - Cycle Detection in Directed Graph

        The problem can be modeled as a directed graph where each course is a node,
        and prerequisites are directed edges. A cycle in this graph would mean an
        impossible sequence of prerequisites.

        Approach:
        1. Build adjacency map where key = course, value = list of prerequisites
        2. Use DFS with visited set to detect cycles
        3. Clear prerequisites after successful DFS to avoid rechecking

        Time Complexity: O(V + E) where V = number of courses, E = number of prerequisites
        Space Complexity: O(V + E) for adjacency map and recursion stack
        """

        # Track visited nodes during current DFS path for cycle detection
        has_visited = set()

        # Build adjacency map: course -> list of prerequisites
        adj_map = {}
        for course, prereq in prerequisites:
            if course in adj_map:
                adj_map[course].append(prereq)
            else:
                adj_map[course] = [prereq]

        def dfs_check_valid(course):
            # No prerequisites for this course
            if course not in adj_map:
                return True

            # Cycle detected - course already in current DFS path
            if course in has_visited:
                return False

            # Course was previously verified
            if adj_map[course] == []:
                return True

            # Mark course as being visited in current path
            has_visited.add(course)

            # Check all prerequisites recursively
            for prereq in adj_map[course]:
                if not dfs_check_valid(prereq):
                    return False

            # Clear prerequisites after verification to avoid rechecking
            adj_map[course] = []

            # Remove course from current path as we backtrack
            has_visited.remove(course)
            return True

        # Check each course that has prerequisites
        for course in adj_map.keys():
            if not dfs_check_valid(course):
                return False

        return True
