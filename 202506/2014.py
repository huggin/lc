class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1

        d = {}
        n = 0
        for i in range(26):
            freq[i] //= k
            if freq[i] > 0:
                d[chr(ord("a") + i)] = freq[i]
                n += freq[i]

        used = defaultdict(int)
        perm = set()

        def dfs(i, curr):
            if i == n:
                perm.add("".join(curr))
                return
            dfs(i + 1, curr)
            for k, v in d.items():
                if v > used[k]:
                    used[k] += 1
                    curr.append(k)
                    dfs(i + 1, curr)
                    curr.pop()
                    used[k] -= 1

        def ok(p):
            n = len(s)
            j = 0
            t = p * k
            for i in range(len(t)):
                while j < n and s[j] != t[i]:
                    j += 1
                if j == n:
                    return False
                j += 1
            return True

        dfs(0, [])

        perm = sorted(perm, key=lambda x: (len(x), x))
        ans = ""
        for p in reversed(perm):
            if ok(p):
                return p

        return ans
