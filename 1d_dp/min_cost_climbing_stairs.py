class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [math.inf] * len(cost)
        costs[len(cost) - 1] = cost[len(cost) - 1]
        costs[len(cost) - 2] = cost[len(cost) - 2]
        for i in range(len(cost) - 3, -1,-1):
            costs[i] = min(costs[i+1] + cost[i],costs[i+2] + cost[i])
        return min(costs[0], costs[1])