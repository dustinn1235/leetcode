class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        alt = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(i,j, visited, prevHeight):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            if (i,j) in visited or heights[i][j] < prevHeight:
                return 
            
            visited.add((i,j))
            dfs(i+1,j,visited,heights[i][j])
            dfs(i-1,j,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    if (i,j) not in pac:
                        dfs(i,j,pac,heights[i][j])

                if i == ROWS - 1 or j == COLS - 1:
                    if (i,j) not in alt:
                        dfs(i,j,alt,heights[i][j])
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        return res

                    