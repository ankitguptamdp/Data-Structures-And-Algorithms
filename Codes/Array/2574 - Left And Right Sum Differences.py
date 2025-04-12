# Last Updated: 12-04-2025 - 07:26 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Prefix Sum

# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        for i in range(1, len(nums)):
            leftSum.append(leftSum[i - 1] + nums[i - 1])
        rightSum = [0] * len(nums)
        for i in range(-2, -len(nums) - 1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]
        output = [abs(leftSum[i] - rightSum[i]) for i in range(len(nums))]
        return output