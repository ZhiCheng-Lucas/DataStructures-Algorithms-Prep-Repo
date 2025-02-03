def validTree(self, n: int, edges: List[List[int]]) -> bool:
    """
    Determines if the given edges form a valid tree with n nodes.

    A valid tree must satisfy two conditions:
    1. No cycles exist (use DFS with parent tracking)
    2. All nodes are connected (number of visited nodes equals total nodes)

    Strategy:
    - Create an adjacency list representation of the graph
    - Use DFS to detect cycles and count visited nodes
    - Node's parent is tracked to avoid false cycle detection in undirected graph

    Time complexity: O(V+E)
    Space complexity: O(V+E)

    """
    # Create adjacency list for undirected graph
    graph = {node: [] for node in range(n)}
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    visited = set()
    nodes_seen = 0

    def dfs(current, parent):
        nonlocal nodes_seen

        # If node was already visited, we found a cycle
        if current in visited:
            return False

        # Mark current node as visited and increment count
        visited.add(current)
        nodes_seen += 1

        # Explore all neighbors except parent
        for neighbor in graph[current]:
            if neighbor != parent:
                if not dfs(neighbor, current):
                    return False

        return True

    # Start DFS from node 0 (parent = -1 since root has no parent)
    if not dfs(0, -1):
        return False

    # Check if all nodes are connected
    return nodes_seen == n
