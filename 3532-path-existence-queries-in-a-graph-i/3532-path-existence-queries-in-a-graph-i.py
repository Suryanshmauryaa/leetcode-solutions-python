class Solution:
    def pathExistenceQueries(self, n: int, nums, maxDiff: int, queries):
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return

            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        # Connect adjacent indices
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                union(i, i - 1)

        ans = []

        for u, v in queries:
            ans.append(find(u) == find(v))

        return ans
        