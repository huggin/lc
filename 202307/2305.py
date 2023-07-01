from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)

        def dfs(i, curr):
            if i == n:
                return max(sum(c) for c in curr)

            ans = 1000000
            flag = True
            for c in curr:
                if len(c) == 0:
                    flag = False
                c.append(cookies[i])
                ans = min(ans, dfs(i + 1, curr))
                c.pop()

            if len(curr) < k and flag:
                curr.append([])
                m = len(curr)
                curr[m - 1].append(cookies[i])
                ans = min(ans, dfs(i + 1, curr))
                curr[m - 1].pop()

            return ans

        curr = []

        return dfs(0, curr)
