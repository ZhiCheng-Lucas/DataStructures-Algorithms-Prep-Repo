class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Algorithm: Process tasks based on frequency with cooldown periods

        Strategy:
        1. Count frequency of each task
        2. Use max heap to always process most frequent tasks first
        3. Use queue to manage tasks on cooldown, storing (frequency, available_time)
        4. Track current time and process tasks/idle as needed

        Time Complexity: O(m), where m is the nunber if tasks
        Space Complexity: O(1), since only have A-Z chars
        """

        # Count frequency of each task
        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1

        # Convert frequencies to negative for max heap implementation
        # using min heap (negative values make it behave like max heap)
        frequencies = [-freq for freq in task_freq.values()]
        heapq.heapify(frequencies)

        current_time = 0
        cooldown_queue = deque()  # Stores (frequency, available_time)

        while frequencies or cooldown_queue:
            # Check if any task in cooldown is now available
            if cooldown_queue:
                next_available_time = cooldown_queue[0][1]
                if current_time == next_available_time:
                    freq_remaining, _ = cooldown_queue.popleft()
                    heapq.heappush(frequencies, freq_remaining)

            # Process most frequent available task
            if frequencies:
                freq = -heapq.heappop(frequencies)  # Convert back to positive
                freq -= 1  # Decrease frequency after processing
                if freq > 0:
                    # If task still has remaining instances, add to cooldown
                    cooldown_queue.append((-freq, current_time + n + 1))

            current_time += 1

        return current_time
