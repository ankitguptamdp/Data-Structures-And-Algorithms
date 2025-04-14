# Last Updated: 14-04-2025 - 07:42 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, String

# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0
        for sentence in sentences:
            countSpace = 1
            for c in sentence:
                if c == " ":
                    countSpace += 1
            if countSpace > output:
                output = countSpace
        return output

# Split Function
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c = 0
        for s in sentences:
            c = max(c, len(s.split()))
        return c