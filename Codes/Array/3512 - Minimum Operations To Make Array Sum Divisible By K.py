# Last Updated: 18-04-2025 - 07:00 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Math

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k