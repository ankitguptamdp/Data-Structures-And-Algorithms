# Last Updated: 11-04-2025 - 08:11 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for hour in hours:
            if hour >= target:
                count += 1
        return count