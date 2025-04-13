# Last Updated: 13-04-2025 - 08:22 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Bit Manipulation

# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        encoded[0] ^= first
        for i in range(1, len(encoded)):
            encoded[i] ^= encoded[i - 1]
        return [first] + encoded

# Another Solution
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        o = [first]
        for i in encoded:
            o.append(i ^ o[-1])
        return o