# Last Updated: 18-04-2025 - 10:13 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array

# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums), 2):
            val = nums[i + 1]
            freq = nums[i]
            output += [val] * freq
        return output

# Using Zip
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [x for a, b in zip(nums[0::2], nums[1::2]) for x in [b] * a]