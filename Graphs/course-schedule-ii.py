class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Finds a valid course ordering that satisfies all prerequisites using topological sort.
        Uses DFS to detect cycles and build the course order.

        Strategy:
        1. Create adjacency map where each course points to its prerequisites
        2. Use DFS with cycle detection to find valid ordering

        Time Complexity: O(V + E) where V is numCourses and E is len(prerequisites)
        Space Complexity: O(V + E) for adjacency map and visited sets
        """
        # Initialize result array and adjacency map for prerequisites
        result = []
        prereq_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # Track visited courses in current DFS path (for cycle detection)
        path_visited = set()
        # Track courses already added to result
        completed = set()

        def dfs(course):
            # Cycle detected - invalid course ordering
            if course in path_visited:
                return False

            # Course has no prerequisites or already processed
            if prereq_map[course] == []:
                if course not in completed:
                    completed.add(course)
                    result.append(course)
                return True

            # Mark course as visited in current path
            path_visited.add(course)

            # Recursively visit all prerequisites
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            # Remove from path (backtrack) and mark prerequisites as completed
            path_visited.remove(course)
            prereq_map[course] = []

            # Add course to result after all prerequisites are satisfied
            completed.add(course)
            result.append(course)
            return True

        # Try to find valid ordering starting from each course
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result
