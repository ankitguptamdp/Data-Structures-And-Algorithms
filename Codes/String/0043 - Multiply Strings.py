class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        result = [0]*(len(num1)+len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for index1 in range(len(num1)):
            for index2 in range(len(num2)):
                digit = int(num1[index1]) * int(num2[index2])
                result[index1+index2] += digit
                result[index1+index2+1] += (result[index1+index2]//10)
                result[index1+index2] = result[index1+index2]%10
        
        result, beginning = result[::-1], 0
        while beginning < len(result) and result[beginning] == 0:
            beginning += 1

        result = map(str, result[beginning:])
        return "".join(result)