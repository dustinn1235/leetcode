class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                edges.append((w,i,j))
        
        par = [i for i in range(len(points))]
        def find(a):
            while a != par[a]:
                par[a] = par[par[a]]
                a = par[a]
            return a

        def union(a,b):
            parA, parB = find(a), find(b)

            if parA == parB:
                return
            par[parA] = parB
        
        cost = 0
        edges.sort(key=lambda edge:edge[0])
        for edge in edges:
            w,u,v = edge
            if find(u) == find(v):
                continue
            cost += w
            union(u,v)
        return cost

