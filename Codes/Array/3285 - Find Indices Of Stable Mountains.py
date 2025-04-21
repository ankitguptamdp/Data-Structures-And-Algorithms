# Last Updated: 21-04-2025 - 05:08 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        output = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                output.append(i)
        return output