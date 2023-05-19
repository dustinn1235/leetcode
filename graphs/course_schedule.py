class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for u,v in prerequisites:
            preMap[u].append(v)

        visited = set()
        def dfs(start):
            if start in visited:
                return False
            if preMap[start] == []:
                return True

            visited.add(start)
            for pre in preMap[start]:
                if not dfs(pre):
                    return False
            visited.remove(start)
            preMap[start] = []
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True

