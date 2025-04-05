# Last Updated: 05-04-2025 - 10:20 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Math

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        return count
