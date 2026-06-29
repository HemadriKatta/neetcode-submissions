from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqMap = {p:[] for p in range(numCourses)}
        inDegree = [0] * numCourses 

        for src, dest in prerequisites:
            preqMap[dest].append(src)
            inDegree[src] += 1
        
        res = [] 
        q = deque()
        for preq in range(numCourses):
            if inDegree[preq] == 0: q.append(preq)

        while q:
            node = q.popleft()
            res.append(node)
            for x in preqMap[node]:
                inDegree[x] -= 1
                if inDegree[x] == 0:
                    q.append(x)
            
        if len(res) != numCourses:
            return []
        
        return res