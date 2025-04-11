# Last Updated: 11-04-2025 - 09:21 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Binary Search, Sorting, Two Pointers

# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count