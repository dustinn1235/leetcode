# traverse in reverse order
# tuple of (pos,speed) sorted by pos
# [(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]
# calculate the time it take to get to target
# if the time of the behind car is less than the ahead car => car will collide => don't add it to the stack
# else add to the stack
# (5,1) can not be in the same fleet with (10,2) but not (8,4).
# if (8,4) is not in the same fleet with (10,2) which mean that it's behind (10,2), otherwise they would be in the same fleet
# Then if (5,1) is in the same fleet with (10,2) => (5,1) is ahead of (8,4) => contradiction

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(key=lambda x: x[0])

        stack = []
        for i in range(len(pairs) - 1, -1, -1):
            timeAtTarget = (target - pairs[i][0]) / pairs[i][1]
            if len(stack) == 0:
                stack.append(timeAtTarget)
            else:
                if timeAtTarget > stack[-1]:
                    stack.append(timeAtTarget)
        return len(stack)