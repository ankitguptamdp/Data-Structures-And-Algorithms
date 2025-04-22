# Last Updated: 22-04-2025 - 10:08 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Hash Table, Sorting, String

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashMap = {}
        for i in range(len(names)):
            hashMap[heights[i]] = names[i]
        heights.sort(reverse=True)
        output = [hashMap[h] for h in heights]
        return output