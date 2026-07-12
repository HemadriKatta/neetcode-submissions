class Solution:
    def isValid(self, s: str) -> bool:
        tempMap = { ')' : '(', ']': '[', '}':'{'}

        res = []
        for st in s:
            if st == '[' or st == '(' or st == '{':
                res.append(st)
            else:
                if res and res[-1] == tempMap[st]:
                    res.pop()
                else: return False
        return len(res) == 0