from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)

        DRAW = 0
        MOUSE = 1
        CAT = 2

        color = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len([x for x in graph[c] if x != 0])

        q = deque()

        for c in range(n):
            for t in range(2):
                color[0][c][t] = MOUSE
                q.append((0, c, t, MOUSE))

        for i in range(1, n):
            for t in range(2):
                color[i][i][t] = CAT
                q.append((i, i, t, CAT))

        while q:
            m, c, turn, result = q.popleft()

            if turn == 0:
                parents = [
                    (m, pc, 1)
                    for pc in graph[c]
                    if pc != 0
                ]
            else:
                parents = [
                    (pm, c, 0)
                    for pm in graph[m]
                ]

            for pm, pc, pt in parents:

                if color[pm][pc][pt] != DRAW:
                    continue

                if (pt == 0 and result == MOUSE) or (pt == 1 and result == CAT):
                    color[pm][pc][pt] = result
                    q.append((pm, pc, pt, result))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        loser = CAT if pt == 0 else MOUSE
                        color[pm][pc][pt] = loser
                        q.append((pm, pc, pt, loser))

        return color[1][2][0]