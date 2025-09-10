class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        lang = list(set(c) for c in languages)
        m = len(lang)
        ans = m
        s = [False] * len(friendships)
        for i, (u, v) in enumerate(friendships):
            if len(lang[u - 1] & lang[v - 1]) > 0:
                s[i] = True
        if False not in s:
            return 0
        for i in range(1, n + 1):
            curr = 0
            temp = list(set() for _ in range(m))
            for j, (u, v) in enumerate(friendships):
                if s[j]:
                    continue
                if (i in lang[v - 1] or i in temp[v - 1]) and (
                    i in lang[u - 1] or i in temp[u - 1]
                ):
                    continue
                elif (i in lang[v - 1] or i in temp[v - 1]) or (
                    i in lang[u - 1] or i in temp[u - 1]
                ):
                    curr += 1
                else:
                    curr += 2
                temp[u - 1].add(i)
                temp[v - 1].add(i)
            ans = min(curr, ans)
        return ans
