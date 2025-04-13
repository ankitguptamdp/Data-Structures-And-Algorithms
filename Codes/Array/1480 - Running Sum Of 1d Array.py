# Last Updated: 13-04-2025 - 07:50 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Prefix Sum

# Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index in range(1, len(nums)):
            nums[index] += nums[index - 1]
        return nums