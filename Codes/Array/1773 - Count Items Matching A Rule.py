# Last Updated: 22-04-2025 - 08:55 AM
# Difficulty: Easy
# Status: Solved
# Tags: Array, String

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleIndex = 0
        if ruleKey == "color":
            ruleIndex = 1
        elif ruleKey == "name":
            ruleIndex = 2
        count = 0
        for item in items:
            if item[ruleIndex] == ruleValue:
                count += 1
        return count

# HashMap
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleIndex = {"type": 0, "color": 1, "name": 2}
        count = 0
        for item in items:
            if item[ruleIndex[ruleKey]] == ruleValue:
                count += 1
        return count