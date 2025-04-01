# Last Updated: 01-04-2025 - 09:38 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Counting, Sorting

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = 0
        for num in nums:
            if num%2 != 0:
                even += 1
        return [0]*(len(nums)-even) + [1]*even