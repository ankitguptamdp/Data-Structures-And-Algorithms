# Last Updated: 21-04-2025 - 05:41 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, String

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
