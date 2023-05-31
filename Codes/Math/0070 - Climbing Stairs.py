class Solution:
    def climbStairs(self, n: int) -> int:
        output = 0
        total = n
        one = n
        two = 0
        while one >=0 and 2*two <= n:
            output += factorial(total)//(factorial(one)*factorial(two))
            total -= 1
            one -= 2
            two += 1
        return output