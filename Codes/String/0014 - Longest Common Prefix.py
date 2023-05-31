class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for index in range(len(strs[0])):
            char = strs[0][index]
            for s in strs:
                if index == len(s) or s[index] != char:
                    return prefix
            prefix += char
        
        return prefix