# Last Updated: 06-04-2025 - 10:03 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Hash Table, Math

# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        output = []
        for key,value in count.items():
            if value == 2:
                output.append(key)
        return output