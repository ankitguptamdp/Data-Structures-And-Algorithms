# Last Updated: 12-04-2025 - 11:18 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Counting Sort, Hash Table, Sorting

# Counting Sort
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * (max(nums) + 1)
        for num in nums:
            count[num] += 1
        leftSum = 0
        for i in range(len(count)):
            cnt = count[i]
            count[i] = leftSum
            leftSum += cnt
        for i in range(len(nums)):
            nums[i] = count[nums[i]]
        return nums