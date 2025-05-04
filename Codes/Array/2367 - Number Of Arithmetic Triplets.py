# Last Updated: 04-05-2025 - 07:48 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Enumeration, Hash Table, Two Pointers

# Brute Force
# Time Complexity: O(n^3)
# Space Complexity: O(1)
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for j in range(1, len(nums) - 1):
            for i in range(0, j):
                for k in range(j + 1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1
        return count
