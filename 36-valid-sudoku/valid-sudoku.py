class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                nums=board[r][c]

                if nums in row[r]:
                    return False
                row[r].add(nums)

                if nums in col[c]:
                    return False 
                col[c].add(nums)

                box=(r//3)*3+(c//3)

                if nums in boxes[box]:
                    return False
                boxes[box].add(nums)

        return True