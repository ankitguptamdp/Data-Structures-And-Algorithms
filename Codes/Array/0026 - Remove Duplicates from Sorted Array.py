# Difficulty: Easy
# Status: Solved
# Tags: Array, Two Pointers
# Time Complexity: O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        for index in range(len(nums)):
            if nums[prev] != nums[index]:
                prev += 1
                nums[prev] = nums[index]
        return prev + 1
