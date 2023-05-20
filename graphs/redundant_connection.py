class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges))]
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
        
        for u,v in edges:
            u,v = u-1,v-1
            if find(u) == find(v):
                return [u+1,v+1]
            union(u,v)

