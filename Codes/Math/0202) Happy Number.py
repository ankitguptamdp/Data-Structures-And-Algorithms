class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            sum = 0
            while n>0:
                sum += (n%10)**2
                n = n//10
            
            if sum == 1:
                return True
            elif sum == 4:
                return False

            n = sum