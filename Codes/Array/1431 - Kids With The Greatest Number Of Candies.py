# Last Updated: 06-04-2025 - 10:43 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        output = []
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                output.append(True)
            else:
                output.append(False)
        return output