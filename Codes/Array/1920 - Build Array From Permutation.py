# Last Updated: 29-03-2025 - 07:05 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Simulation

# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        for index in range(len(nums)):
            output[index] = nums[nums[index]]
        return output

# Using
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] += 1001*(nums[nums[i]]%1001)
        for i in range(len(nums)):
            nums[i] //= 1001
        return nums