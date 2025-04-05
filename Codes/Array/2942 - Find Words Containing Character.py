# Last Updated: 05-04-2025 - 10:54 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, String

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for index in range(len(words)):
            if x in words[index]:
                output.append(index)
        return output
