class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        v = [0] * (n + 1)

        def dfs(k):
            if k > n or v[k] == 1:
                return
            v[k] = 1
            ans.append(k)
            for i in range(10):
                dfs(k * 10 + i)
            if (k + 1) % 10 != 0:
                dfs(k + 1)

        dfs(1)

        return ans
