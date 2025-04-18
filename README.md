# DataStructures-Algorithm-Prep

A personal repository documenting my daily journey through LeetCode problems.
Each question is divided into its separate Python file and contains a brief explanation of the question, my thoughts on the solution and explanation, as well as the expected time and space complexity, along with comments in the code.

Useful links:
<https://neetcode.io/roadmap>
<https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/>
<https://datalemur.com/sql-tutorial/query-order-of-execution>

## SQL Info

### Order of execution

1. FROM clause (including JOINs with ON conditions)
2. WHERE clause
3. GROUP BY clause
4. HAVING clause
5. SELECT clause
6. ORDER BY clause
7. LIMIT/OFFSET clauses

### Order of writing

1. SELECT clause (columns to retrieve)
2. FROM clause (tables to query)
3. JOIN clauses with ON conditions (table relationships)
4. WHERE clause (row filtering conditions)
5. GROUP BY clause (aggregation)
6. HAVING clause (filtering aggregated results)
7. ORDER BY clause (sorting results)
8. LIMIT/OFFSET clauses (restricting number of results)

### General info

For rounding to decimal, requires ":: numeric"
ROUND(value::numeric, decimal_places)

### Date

-- Add 1 day
SELECT date_column + INTERVAL '1 day' FROM table_name;

-- Add 3 months
SELECT date_column + INTERVAL '3 months' FROM table_name;

-- Add multiple intervals
SELECT date_column + INTERVAL '1 year 2 months 3 days' FROM table_name;

# Coding question patterns for all relevant DSA types

[ARRAYS](#arrays)

1. Two Pointers: Used for finding pairs or elements that meet specific criteria.
2. Sliding Window: Maintains a subset of elements within a larger dataset.
3. Binary Search: Efficient searching in sorted arrays.
4. Prefix Sum: Precompute cumulative sums for quick range queries.
5. Stacks and queues - LIFO/FIFO data structures

    [STACKS](#stacks)

    1. Parentheses matching: Validate balanced brackets.
    2. Monotonic stack: Maintain increasing/decreasing order for next greater/smaller element problems.
    3. Expression evaluation: Evaluate arithmetic expressions.

    [QUEUES](#queues)

    1. BFS implementation: Level-order traversal in graphs and trees.
    2. Task scheduling: Manage order of operations.
    3. Sliding window problems: Maintain a window of elements.

[STRINGS](#strings)

1. Trie/prefix tree - Character-based search tree (Word Search)
2. Count number of frequencies - Hashmap character counting

[TREES](#trees)

1. Depth-First Search (DFS): Preorder, inorder, and postorder traversals.
2. Breadth-First Search (BFS): Level-order traversal.
3. Binary Search Tree (BST) operations: Insertion, deletion, and validation.
4. Tree construction: From preorder/inorder or postorder/inorder traversals.

[HASHTABLES](#hashtables)

1. Frequency counting: Track occurrences of elements.
2. Two Sum pattern: Find pairs with a specific sum.
3. Anagram detection: Compare character frequencies.
4. Caching: Store computed results for quick lookup.

[GRAPHS](#graphs)

1. Depth-First Search (DFS): Explore paths deeply before backtracking.
2. Breadth-First Search (BFS): Explore nodes level by level.
3. Topological Sort: Order nodes in a directed acyclic graph.
4. Union Find: Detect cycles and connect components.
5. Adjacency matrix (dfs / bfs) - Grid representation
6. Adjacency list - Node-edge representation
7. Topological sort - Directed dependency ordering
8. Dijkstra - Shortest path algorithm
9. Prim - Minimum spanning tree
10. Kruskal - Minimum spanning tree via edges

[HEAPS](#heaps)

1. Top K Elements Pattern: Find or manipulate the K largest/smallest elements in a collection.
2. Merge K Sorted Pattern: Combine K sorted lists or arrays into a single sorted list.
3. Two Heaps Pattern: Use two heaps to track median or balance elements in a stream.
4. Sliding Window Median Pattern: Calculate median in a sliding window over a stream of numbers.
5. Scheduling Pattern: Manage tasks or intervals using a heap for efficient scheduling.

[BACKTRACKING](#backtracking)

1. **Subsets** - Generate all possible subsets
   * Creates every possible subset from a given set, including empty set and the complete set.

2. **Permutation** - Generate all possible arrangements (Order matters - 123 and 321 are different)
   * P(n,r) = n! / (n-r)!
   * This formula calculates the number of ways to arrange r items from a set of n items where order matters. Unlike combinations, each different arrangement counts as a distinct permutation.

3. **Combination** - Generate specific groupings (Order doesn't matter - 123 and 321 are the same)
   * C(n,r) = n! / [r! × (n-r)!]
   * This formula calculates the number of ways to select r items from a set of n items where order doesn't matter. The factorials account for all possible arrangements being counted as a single combination.

4. **Tree maze** - Path finding with constraints
   * Navigates through decision trees to find paths that satisfy given constraints.

[GREEDY](#greedy)

1. Kandane - Maximum subarray sum

[LINKED LISTS](#linked-lists)

1. Singly linked lists - One-directional node connections
2. Doubly linked lists - Bidirectional node connections
3. Fast and slow pointers - Cycle detection technique

## ARRAYS

## STACKS

## QUEUES

## STRINGS

## TREES

## HASHTABLES

## GRAPHS

## HEAPS

## BACKTRACKING

## GREEDY

## LINKED LISTS

Dynamic programming - Optimization via subproblems
Time Management (20 min per question)

5 min: Problem understanding, edge cases, clarifying questions
5 min: Pseudocode + example walkthrough
5 min: Coding implementation
5 min: Optimization discussion & complexity analysis

Follow the UPED framework:
Understand
Plan
Execute
Discuss

General Info:

In Python classes, self refers to the instance of the class that's being created or operated on. It's a way for the object to reference itself

For questions involving deep copies etc.
Consider creating a hashmap with the old node as the key and the newly created node as the value.

lambda functions.
lambda x,y: x+y
Before the : represents the input. After the : represents the output or the expression.
eg.
intervals = [[1,2], [2,1]]
intervals.sort(key=lambda interval:interval[1])
interval is the input (same as i in for i in intervals) and it will return interval[1] as the sorting key which is 2 and 1.
Hence, it will be sorted into [[2,1] [1,2]]

Stacks:

Consider when:
Expression Evaluation and Parsing or just Evaluation.

1. Last-In-First-Out
2. State/History Tracking
3. Nested/Hierarchical
    * A stack is ideal because it naturally tracks the "most recently opened" item
    * Expression Evaluation and Parsing can fall under this as expression has inherent nesting through parentheses, and the order of operations creates a natural hierarchy

Common use case include:

* Expression Evaluation and Parsing
* Depth-First Search (DFS) Implementation
* Call stack management

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

Heaps:
heapify is a o(n) function
When talking about maximum/ minimum qns, consider a heap approach. See heapq in python.
To simulate a maxheap in python, use negative values instead.
eg. [2,3,4] becomes [-2,-3,-4]
so 4 would be the minimum value.

A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest (or lowest) priority, or when insertions need to be interspersed with removals of the root node.

Mention of k
If you see a top or lowest k being mentioned in the question, it is usually a signal that a heap can be used to solve the problem, such as in Top K Frequent Elements.

If you require the top k elements use a Min Heap of size k. Iterate through each element, pushing it into the heap (for python heapq, invert the value before pushing to find the max). Whenever the heap size exceeds k, remove the minimum element, that will guarantee that you have the k largest elements.

Backtracking:
For combination/permutation problems, subset problems.
Consider backtracking.

Draw a decision tree.
Then dfs.

Example.

```

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Generate all possible subsets using a backtracking approach.
        
        For each element in nums, we make a binary choice:
        1. Include the current element in the subset
        2. Exclude the current element from the subset
        
        This creates a binary decision tree where:
        - Each level represents a position in nums
        - Left branch: include current number
        - Right branch: exclude current number
        
        Example with [1,2,3]:
                        []
                /              \
            [1]                []
          /      \           /    \
        [1,2]    [1]       [2]    []
        /  \     /  \     /  \    / \
      [123][12][13][1]  [23][2] [3][]
        
        Time complexity: O(2^n) - we make 2 choices for each element
        Space complexity: O(n) - max recursion depth equals array length
        '''
        res = []        # Store all valid subsets
        subset = []     # Current subset being built
        
        def dfs(i):
            # Base case: processed all elements
            if i >= len(nums):
                res.append(subset.copy())    # Add the complete subset
                return
            
            # Decision 1: Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision 2: Exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)    # Start from index 0
        return res
```

Intervals:

* It might be helpful to draw a number line to visualize
* Useful to sort based on START time.
They don't overlap when either:

A ends before B starts: A[end] < B[start]
B ends before A starts: B[end] < A[start]

Therefore, they DO overlap when NEITHER of these is true. In other words, they overlap when:

A doesn't end before B starts: A[end] >= B[start]
AND
B doesn't end before A starts: B[end] >= A[start]

Graphs:
2D matrix.
Adjacency list

Dynamic Programming

1. Optimal substructure. - Optimal solution to subproblem lead to the optimal solution
2. Overlapping subproblem

Some indicators are

1. Sequential decision-making
2. Greedy choice property
3. State transition
4. Path or array.
5. Counting or maximization/minimization

Here's the text version of the recursion lecture slide:

# Recursion

## Structure → Technique

### Start with the recurrence relation

* Base case??? For what problem?
* Actions → Recursive calls
* Consequences → Transitions
* Contributions → Return Value
* Affected variables → Parameters

### Obey the rules of recursion

1. Base cases must be correct
2. Recursive calls shrink to a base case
3. Assume recursive calls are correct

### Build base cases from the calls

* Name the function on its promises!
* Avoid simulating/visualizing, it's painful
* Recursion is naturally inductive
* Read aloud and see if it makes sense

### Main Ideas

Technique requires a solid understanding of where, why, and how.

### Recursion

* Where: Subtasks have the same shape
* Why: To simplify a problem with induction
* How: Use induction!!!

### Additional Guidelines

* Do not think more than 1 recurrence down
* Name a function on it promises to do
* No prints or simulation, just read it aloud!

# Dynamic Programming

*Technique → More Technique*

## Requirements

* Must have a recurrence relation
  * Function must be pure: no side effects
* Recurrence Relation < Recursive Execution

## Time Complexity

* (# Unique States) * (Cached Complexity)

* # Unique States

  * Size of recurrence relation
  * Usually the product of parameter bounds
* Cached Complexity
  * What's the time complexity assuming recursive calls are O(1)?

## DP = Decision Parameterization

* Decisions are values to compute once
* Decisions are not tasks to run every time
* More Parameters → Higher Runtime
* Minimize the parameters needed for a decision
* Minimize the time to complete the decision

## Main Ideas

* Recurrence relation != Recursive execution
* A recurrence relation is a mathematical construct:
  * It does not have side effects
  * It does not "compute" anything
  * It does not require recursive execution
  * It's just a relationship between states

## Dynamic programming

* Decomposes problems with recurrence relations
* Recursive terms are values calculated once
* Evaluates in a valid order of dependencies
