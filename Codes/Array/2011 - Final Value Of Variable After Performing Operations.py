# Last Updated: 30-03-2025 - 11:04 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, String, Simulation

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for operation in operations:
            if operation in ('++X', 'X++'):
                count += 1
            else:
                count -= 1
        return count