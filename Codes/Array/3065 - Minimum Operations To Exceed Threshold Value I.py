# Last Updated: 15-04-2025 - 09:52 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        output = 0
        for num in nums:
            if num < k:
                output += 1
        return output
