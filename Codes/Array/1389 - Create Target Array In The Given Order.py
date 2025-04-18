# Last Updated: 18-04-2025 - 08:43 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Simulation

# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target

# Another Solution
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            if len(target) == index[i]:
                target.append(nums[i])
            else:
                target.insert(index[i], nums[i])
        return target

# Without Insert Function
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            if len(target) == index[i]:
                target.append(nums[i])
            else:
                target = target[: index[i]] + [nums[i]] + target[index[i] :]
        return target

