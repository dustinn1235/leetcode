# max heap 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while (len(stones) > 1):
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1

            if x != y:
                y -= x
                y = y * -1
                heapq.heappush(stones,y)
        print(stones)
        if len(stones) == 0:
            return 0
        else:
            return stones[0] * -1