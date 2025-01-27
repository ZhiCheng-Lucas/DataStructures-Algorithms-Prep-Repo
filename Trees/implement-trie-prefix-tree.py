class TrieNode:
    def __init__(self):
        # Dictionary to store character children
        self.children = {}
        # Flag to mark if this node represents end of a word
        self.isEndOfWord = False


class Trie:
    """
    A Trie (prefix tree) implementation for efficient string storage and retrieval.
    Time Complexity: Insert/Search/StartsWith - O(m) where m is word length
    Space Complexity: O(t) where t is the total number of TrieNode
    """

    def __init__(self):
        # Initialize root node of Trie
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the Trie"""
        current = self.root

        # Build the word path in Trie, creating new nodes as needed
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        # Mark the last node as end of word
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        """Check if the word exists in the Trie"""
        current = self.root

        # Follow the word path in Trie
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        # Word exists only if we reach an end-of-word node
        return current.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """Check if any word in Trie starts with given prefix"""
        current = self.root

        # Follow the prefix path in Trie
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        # If we can follow all characters in prefix, it exists
        return True


# Example usage:
# trie = Trie()
# trie.insert("apple")        # Insert "apple"
# trie.search("apple")        # Returns True
# trie.search("app")          # Returns False
# trie.startsWith("app")      # Returns True
