class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(temperatures)):
            maxTemp = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    stack.append(maxTemp)
                    break
                elif j == len(temperatures) - 1:
                    stack.append(0)
                else:
                    maxTemp += 1
        stack.append(0)
                
        return stack
                    
            
            
                
                



        