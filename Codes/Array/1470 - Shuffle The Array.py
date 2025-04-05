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

# Bit Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for index in range(n):
            nums[index] = nums[index] << 10
            nums[index] = nums[index] | nums[index+n]
        for index in range(n):
            nums[-2*index-1] = nums[n-index-1] & (2**10-1)
            nums[-2*index-2] = nums[n-index-1] >> 10
        return nums