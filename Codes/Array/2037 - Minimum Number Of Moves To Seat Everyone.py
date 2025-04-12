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

# Counting Sort
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_index = max(max(seats), max(students)) + 1
        count_seats = [0] * max_index
        count_students = [0] * max_index
        for seat in seats:
            count_seats[seat] += 1
        for student in students:
            count_students[student] += 1
        i, j = 0, 0
        res = 0
        remain = len(students)
        while remain:
            if count_seats[i] == 0:
                i += 1
            if count_students[j] == 0:
                j += 1
            if count_seats[i] and count_students[j]:
                res += abs(i - j)
                count_seats[i] -= 1
                count_students[j] -= 1
                remain -= 1
        return res
