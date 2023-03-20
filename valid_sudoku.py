# check if every cols, rows has duplicate by set
# map coor to the square section.
# (1,1) => first square => 1//3, 1//3 => 0,0
# (9,9) => last row, last col square => 9//3, 9//3 => 3,3

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                x = board[r][c]
                if (x == "."):
                    continue
                if (x in rows[r] or x in cols[c] or x in squares[(r//3,c//3)]):
                    return False
                cols[c].add(x)
                rows[r].add(x)
                squares[(r//3,c//3)].add(x)
        return True