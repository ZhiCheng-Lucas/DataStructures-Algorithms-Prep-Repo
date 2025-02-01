class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Graph Clone (Deep Copy):
        Given a reference node in an undirected connected graph, create a deep copy of the entire graph.
        Each node contains a value and a list of references to its neighbors.

        Strategy:
        Use DFS with a hash map to handle cycles and avoid infinite recursion. The hash map tracks
        which nodes have already been cloned by mapping original nodes to their cloned copies.

        Time Complexity: O(N + E) where N is number of nodes and E is number of edges
                         We visit each node once and process all edges
        Space Complexity: O(N) for the hash map and recursion stack
        """
        original_to_clone = {}  # Maps original nodes to their cloned copies

        def dfs(node):
            if not node:
                return None

            if node in original_to_clone:
                return original_to_clone[node]  # Return existing clone to handle cycles

            # Create new node and map it before processing neighbors
            clone = Node(node.val)
            original_to_clone[node] = clone  # Must store before DFS to handle cycles

            # Recursively clone each neighbor and add to the new node's neighbor list
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
