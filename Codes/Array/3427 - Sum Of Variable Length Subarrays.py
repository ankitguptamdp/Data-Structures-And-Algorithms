# Last Updated: 20-04-2025 - 08:43 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Prefix Sum

# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            output += sum(nums[start : i + 1])
        return output