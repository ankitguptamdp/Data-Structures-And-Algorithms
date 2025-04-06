# Last Updated: 06-04-2025 - 05:14 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Bit Manipulation, Counting, Hash Table, String

# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            consistent = True
            for ch in word:
                if ch not in allowed:
                    consistent = False
                    break
            if consistent:
                count += 1
        return count