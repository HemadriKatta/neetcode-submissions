class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, ele in enumerate(temperatures):
            while stack  and ele > stack[-1][0]:
                temp, tempInd = stack.pop()
                res[tempInd] = i - tempInd
            stack.append((ele, i))
        return res

                    
            
            
                
                



        