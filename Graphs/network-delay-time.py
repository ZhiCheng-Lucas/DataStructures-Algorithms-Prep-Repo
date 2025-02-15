class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Finds the minimum time for a signal to reach all nodes in a network using Dijkstra's algorithm.

        The problem represents a weighted directed graph where:
        - Each edge (u,v,w) represents a signal path from node u to v taking w time
        - We need to find how long it takes for a signal from node k to reach all other nodes

        Strategy:
        1. Build adjacency list representation of the graph
        2. Use min heap to always process node with minimum current time
        3. Keep track of visited nodes and maximum time taken
        4. Return -1 if not all nodes are reachable

        Time: O(E * logV) where E is number of edges, V is number of vertices
        Space: O(V + E) for graph and heap
        """
        # Create adjacency list representation of the graph
        graph = {i: [] for i in range(1, n + 1)}
        for source, target, time in times:
            graph[source].append((target, time))

        # Min heap to process nodes in order of cumulative time
        # Each entry is (total_time_to_reach, node)
        min_heap = [(0, k)]
        visited = set()
        max_time = 0  # Tracks time for signal to reach furthest node

        while min_heap:
            curr_time, curr_node = heappop(min_heap)
            if curr_node in visited:
                continue

            visited.add(curr_node)
            max_time = max(max_time, curr_time)

            # Explore all neighbors of current node
            for next_node, travel_time in graph[curr_node]:
                if next_node not in visited:
                    total_time = curr_time + travel_time
                    heappush(min_heap, (total_time, next_node))

        # If we couldn't visit all nodes, signal can't reach everyone
        return max_time if len(visited) == n else -1
