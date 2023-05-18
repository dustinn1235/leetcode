class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        time = 0
        while q and fresh > 0:
            for tmp in range(len(q)):
                i,j = q.popleft()
                for di,dj in directions:
                    dirI = i + di
                    dirJ = j + dj
                    if dirI < 0 or dirI >= len(grid) or dirJ < 0 or dirJ >= len(grid[0]):
                        continue
                    
                    if grid[dirI][dirJ] == 1:
                        fresh -=1
                        grid[dirI][dirJ] = 2
                        q.append((dirI,dirJ))
            time += 1
        return time if fresh == 0 else -1
                
