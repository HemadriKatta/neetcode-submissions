from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = defaultdict(list)
        for src, dest in prerequisites:
            preqMap[src].append(dest)
        
        visited = set()

        def dfs(p):
            if p in visited: return False
            if preqMap[p] == []: return True

            visited.add(p)
            for preq in preqMap[p]:
                if not dfs(preq): return False
            
            visited.remove(p)
            return True

        for p in range(numCourses):
            if not dfs(p): return False
        
        return True
        