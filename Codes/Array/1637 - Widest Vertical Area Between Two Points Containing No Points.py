# Last Updated: 13-04-2025 - 12:48 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Sorting

# Counting Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        widestVerticalArea = 0
        for i in range(len(points) - 1):
            if points[i + 1][0] - points[i][0] > widestVerticalArea:
                widestVerticalArea = points[i + 1][0] - points[i][0]
        return widestVerticalArea