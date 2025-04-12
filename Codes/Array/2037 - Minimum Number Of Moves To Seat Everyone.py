# Last Updated: 12-04-2025 - 09:11 AM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Counting Sort, Greedy, Sorting

# Greedy
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        output = 0
        for i in range(len(seats)):
            output += abs(seats[i] - students[i])
        return output
