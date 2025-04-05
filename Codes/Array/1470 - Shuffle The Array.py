# Last Updated: 05-04-2025 - 07:21 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array

# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for index in range(n):
            output.append(nums[index])
            output.append(nums[n + index])
        return output