class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        NEG = -1

        score = [[NEG] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                best = NEG
                count = 0

                for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if x < n and y < n:
                        if score[x][y] > best:
                            best = score[x][y]
                            count = ways[x][y]
                        elif score[x][y] == best and best != NEG:
                            count = (count + ways[x][y]) % MOD

                if best == NEG:
                    continue

                value = 0
                if board[i][j].isdigit():
                    value = int(board[i][j])

                score[i][j] = best + value
                ways[i][j] = count % MOD

        if ways[0][0] == 0:
            return [0, 0]

        return [score[0][0], ways[0][0]]