class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqMap = {p:[] for p in range(numCourses)}

        for src, dest in prerequisites:
            preqMap[src].append(dest)
        
        res = [] 
        visited, cycle = set(), set()

        def dfs(preq):
            if preq in cycle: return False
            if preq in visited: return True

            cycle.add(preq)
            for p in preqMap[preq]:
                if dfs(p) == False: return False
            cycle.remove(preq)
            visited.add(preq)
            res.append(preq)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res
            

        