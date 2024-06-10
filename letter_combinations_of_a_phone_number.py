class Solution(object):
    def printLetter(self, word, index, result, bigResult):
        store = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
        }
        if index == len(word):
            bigResult.append("".join(result))
            return 
 
        ch = word[index]
        for val in store[ch]:
            result.append(val)
            self.printLetter(word, index + 1, result, bigResult)
            result.pop()
 
    def letterCombinations(self, digits):
        bigResult = []
        if len(digits) == 0:
            return bigResult
        result = []
        self.printLetter(digits, 0, result, bigResult)
        return bigResult
