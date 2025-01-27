# DataStructures-Algorithm-Prep
A personal repository documenting my daily journey through LeetCode problems.

Each question is divided into its separate Python file and contains a brief explanation of the question, my thoughts on the solution and explanation, as well as the expected time and space complexity, along with comments in the code.


General Info:


In Python classes, self refers to the instance of the class that's being created or operated on. It's a way for the object to reference itself


Stacks: 

Consider when:
Expression Evaluation and Parsing or just Evaluation.

1. Last-In-First-Out
2. State/History Tracking
3. Nested/Hierarchical 
    - A stack is ideal because it naturally tracks the "most recently opened" item
    - Expression Evaluation and Parsing can fall under this as expression has inherent nesting through parentheses, and the order of operations creates a natural hierarchy

Common use case include:
- Expression Evaluation and Parsing
- Depth-First Search (DFS) Implementation
- Call stack management


2-pointer:
When it is a SORTED array.

For 2pointer or sliding window, can consider trying a graph for better visualization of the problem.

Linked List Info:

Sentinel/dummy nodes:
Adding a sentinel/dummy node at the head and/or tail might help to handle many edge cases where operations have to be performed at the head or the tail. The presence of dummy nodes essentially ensures that operations will never be done on the head or the tail, thereby removing a lot of headache in writing conditional checks to dealing with null pointers. Be sure to remember to remove them at the end of the operation.

Two pointers:
1. Getting the kth from last node - Have two pointers, where one is k nodes ahead of the other. When the node ahead reaches the end, the other node is k nodes behind
2. Detecting cycles - Have two pointers, where one pointer increments twice as much as the other, if the two pointers meet, means that there is a cycle
3. Getting the middle node - Have two pointers, where one pointer increments twice as much as the other. When the faster node reaches the end of the list, the slower node will be at the middle

Using space:
Many linked list problems can be easily solved by creating a new linked list and adding nodes to the new linked list with the final result. However, this takes up extra space and makes the question much less challenging. 








All recursive functions contains two parts:

A base case (or cases) defined, which defines when the recursion is stopped - otherwise it will go on forever!
Breaking down the problem into smaller subproblems and invoking the recursive call

```def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case    
    return n * factorial(n-1)
```

```
def recursive_function(input):
    # Base case
    if [smallest possible input]:
        return [solution for base case]
    
    # Recursive case
    # 1. Make recursive call
    result = recursive_function(smaller_input)
    # 2. Use result to solve current step
    # 3. Return solution
```


Trees.

For prefix matching etc, can consider a trie data structure 

DFS - Stack (inorder, preorder and postorder)
BFS - FIFO queue

```
def inorder_traversal(node):
    if node:
        # First traverse left subtree
        inorder_traversal(node.left)
        # Then visit the root
        print(node.value)
        # Finally traverse right subtree
        inorder_traversal(node.right)
```

```
def preorder_traversal(node):
    if node:
        # First visit the root
        print(node.value)
        # Then traverse left subtree
        preorder_traversal(node.left)
        # Finally traverse right subtree
        preorder_traversal(node.right)

```

```
def postorder_traversal(node):
    if node:
        # First traverse left subtree
        postorder_traversal(node.left)
        # Then traverse right subtree
        postorder_traversal(node.right)
        # Finally visit the root
        print(node.value)
```