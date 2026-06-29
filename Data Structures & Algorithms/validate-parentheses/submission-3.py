class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sampleDict = { ')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in sampleDict:
                lastEle = stack.pop() if stack else '#'
                if lastEle != sampleDict[i]:
                    return False
            else:
                stack.append(i)
        
        return not stack


