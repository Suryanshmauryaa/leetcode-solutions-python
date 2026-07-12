import math

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # Sort (value, original_index)
        arr = sorted((v, i) for i, v in enumerate(nums))

        sorted_nums = [v for v, _ in arr]

        # original index -> position in sorted order
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        LOG = n.bit_length() + 1

        # jump[i][k] = position reached after 2^k greedy jumps
        jump = [[0] * LOG for _ in range(n)]

        # Furthest reachable position in one jump
        r = 0
        for l in range(n):
            while r + 1 < n and sorted_nums[r + 1] - sorted_nums[l] <= maxDiff:
                r += 1
            jump[l][0] = r

        # Binary lifting table
        for k in range(1, LOG):
            for i in range(n):
                jump[i][k] = jump[jump[i][k - 1]][k - 1]

        def min_jumps(start, end):
            if start == end:
                return 0

            if jump[start][0] >= end:
                return 1

            if jump[start][LOG - 1] < end:
                return -1

            ans = 0
            cur = start

            for k in range(LOG - 1, -1, -1):
                if jump[cur][k] < end:
                    ans += 1 << k
                    cur = jump[cur][k]

            return ans + 1

        res = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            res.append(min_jumps(a, b))

        return res