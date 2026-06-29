class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numLetters = {
            '2' : 'abc',
            '3' : 'def', 
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        res = []
        if digits == '': return res
        def backtrack(idx, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for i in numLetters[digits[idx]]:
                backtrack(idx + 1, curr +  i)
            
        backtrack(0, '')
        return res