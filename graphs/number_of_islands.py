class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(start):
            nonlocal visited
            visited.add(start)
            i,j = start
            neighs = []

            if i != 0 and grid[i - 1][j] == "1":
                neighs.append((i-1, j))
            if i != len(grid) - 1 and grid[i+1][j] == "1":
                neighs.append((i+1, j))
            if j != 0 and grid[i][j-1] == "1":
                neighs.append((i, j - 1))
            if j != len(grid[0]) - 1 and grid[i][j+1] == "1":
                neighs.append((i, j + 1))
            
            for neigh in neighs:
                if neigh not in visited:
                    dfs(neigh)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs((i,j))
                    print()
                    res += 1
        return res

        