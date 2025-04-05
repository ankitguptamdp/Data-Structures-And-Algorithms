# Last Updated: 05-04-2025 - 10:54 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, Matrix

# Time Complexity: O(m*n)
# Space Complexity: O(1)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = 0
        for i in range(len(accounts)):
            amount = 0
            for j in range(len(accounts[i])):
                amount += accounts[i][j]
            if amount > output:
                output = amount
        return output