# add to temp to the stack. pop the stack if cur temp > stack.top. Put the res in stack.top index by i - stack.top index
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while len(stack) != 0 and temp > stack[-1][1]:
                sIndex, sTemp = stack.pop()
                res[sIndex] = i - sIndex
            stack.append((i,temp))
        return res