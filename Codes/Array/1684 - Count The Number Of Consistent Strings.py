# Last Updated: 06-04-2025 - 05:14 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Bit Manipulation, Counting, Hash Table, String

# Brute Force
# Time Complexity: O(n*m)
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

# Hash Table
# Time Complexity: O(n*m)
# Space Complexity: O(1)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
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

# Bit Manipulation
# Time Complexity: O(n*m)
# Space Complexity: O(1)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        bit_mask = 0
        for c in allowed:
            bit = 1 << ord(c) - ord("a")
            bit_mask = bit_mask | bit
        count = 0
        for word in words:
            consistent = True
            for ch in word:
                bit = 1 << ord(ch) - ord("a")
                if bit & bit_mask == 0:
                    consistent = False
                    break
            if consistent:
                count += 1
        return count

# Bit Manipulation
# Time Complexity: O(n*m)
# Space Complexity: O(1)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bit_mask = 0
        for c in allowed:
            bit = 1 << (ord(c) - ord("a"))
            bit_mask = bit_mask | bit
        count = len(words)
        for word in words:
            for c in word:
                bit = 1 << ord(c) - ord("a")
                if bit & bit_mask == 0:
                    count -= 1
                    break
        return count