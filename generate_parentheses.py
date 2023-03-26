class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(comb, openN, closeN):
            if openN == n and openN == closeN:
                res.append(comb)
                return
            if openN < n:
                backtrack(comb + "(", openN + 1, closeN)
            if closeN < openN:
                backtrack(comb + ")", openN, closeN + 1) 
        backtrack("", 0, 0)
        return res