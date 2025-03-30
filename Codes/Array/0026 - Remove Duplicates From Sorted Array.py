# Last Updated: 25-02-2025 - 08:53 AM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        for index in range(len(nums)):
            if nums[prev] != nums[index]:
                prev += 1
                nums[prev] = nums[index]
        return prev + 1
