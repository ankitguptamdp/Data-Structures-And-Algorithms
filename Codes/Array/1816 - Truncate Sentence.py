# Last Updated: 20-04-2025 - 05:51 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, String

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
