class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for u,v in prerequisites:
            preMap[u].append(v)
        
        memo = [-1] * numCourses
        visited = set()
        res = []
        def dfs(start):
            if memo[start] != -1:
                return True if memo[start] == 1 else False
            if start in visited:
                memo[start] = 0
                return False
            if preMap[start] == []:
                res.append(start)
                memo[start] = 1
                return True
            
            visited.add(start)
            for pre in preMap[start]:
                if not dfs(pre):
                    return False
            res.append(start)
            memo[start] = 1
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        return res