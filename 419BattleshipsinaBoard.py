#77.69
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if board == [] or len(board[0]) == 0:
            return 0
        result = 0

        for i in range(len(board[0])):
            if board[0][i] == "X":
                if i > 0 and board[0][i - 1] == "X":
                    continue
                result += 1

        for i in range(1, len(board)):
            if board[i][0] == "X":
                if i > 0 and board[i - 1][0] == "X":
                    continue
                result += 1

        for i in range(1, len(board)):
            for j in range(1, len(board[0])):
                if board[i][j] == "X":
                    if board[i - 1][j] == "X":
                        continue
                    if board[i][j - 1] == "X":
                        continue
                    result += 1

        return result

