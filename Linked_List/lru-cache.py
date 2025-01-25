class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        # Links for doubly linked list
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache implementation using a hashmap and doubly linked list.
    The hashmap provides O(1) access while the doubly linked list maintains order.

    Design approach:
    - Use hashmap to store key -> Node mappings for O(1) lookup
    - Use doubly linked list to track access order (MRU to LRU)
    - Dummy nodes (left, right) simplify edge cases in list operations
    - Most recently used items are near 'right', least recently near 'left'

    Time Complexity: O(1) for both get and put operations
    Space Complexity: O(capacity) to store cache items
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Hashmap for O(1) key lookups

        # Initialize dummy nodes to avoid edge cases
        self.left = Node(0, 0)  # LRU sentinel
        self.right = Node(0, 0)  # MRU sentinel
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Remove node from doubly linked list
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        # Always insert before right dummy node (MRU position)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to most recently used position
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # Remove existing key if present
        if key in self.cache:
            self.remove(self.cache[key])

        # Create and insert new node
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Evict least recently used if capacity exceeded
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
