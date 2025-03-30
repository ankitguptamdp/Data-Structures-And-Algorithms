# Last Updated: 29-03-2025 - 09:00 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Counting, Hash Table, Math

# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    output += 1
        return output

# Using Hash Table And Maths
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        output = 0
        for key,value in frequency.items():
            output += value*(value-1)//2
        return output

# Using Hash Table
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = {}
        output = 0
        for num in nums:
            if num in frequency:
                output += frequency[num]
                frequency[num] += 1
            else:
                frequency[num] = 1
        return output