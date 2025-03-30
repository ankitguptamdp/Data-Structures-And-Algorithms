# Last Updated: 30-03-2025 - 08:11 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        prev = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[prev] = nums[index]
                prev += 1
        return prev
