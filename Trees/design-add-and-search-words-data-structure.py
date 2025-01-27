class Node:
    def __init__(self):
        # Dictionary to store child nodes, where key is the character and value is the Node
        self.children = {}
        # Flag to mark if this node represents the end of a word
        self.isLastNode = False


class WordDictionary:
    """
    A trie-based data structure that supports adding words and searching with wildcards.
    The trie (prefix tree) enables efficient prefix matching and wildcard searching.

    Time Complexity:
    - Add: O(m) where m is the length of the word
    - Search: O(m)

    Space Complexity: O(t) where t is the number of Nodes
    """

    def __init__(self):
        # Initialize root node of the trie
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        # Build trie by adding nodes for each character
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]

        # Mark the last node as end of word
        curr.isLastNode = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            """
            Depth-first search to handle both normal characters and wildcards.
            Returns True if word[index:] exists in trie starting from root.
            """
            current = root

            for i in range(index, len(word)):
                char = word[i]

                if char == ".":
                    # For wildcard, try all possible children
                    # Return True if any path leads to a match
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # For normal character, follow the specific path
                    if char not in current.children:
                        return False
                    current = current.children[char]

            # Return whether we've found a complete word
            return current.isLastNode

        return dfs(0, self.root)
