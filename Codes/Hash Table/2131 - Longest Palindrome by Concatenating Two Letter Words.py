class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dictionary = {}
        result = 0

        for word in words:
            dictionary[word] = dictionary.get(word, 0) + 1

        for key,value in dictionary.items():
            if key in dictionary and key[::-1] in dictionary:
                if key == key[::-1]:
                    result += ((value//2)*2*2)
                elif key < key[::-1]:
                    result += (min(value, dictionary[key[::-1]])*4)
        
        for key, value in dictionary.items():
            if key[0]==key[1] and value%2 == 1:
                result +=2
                break
       
        return result