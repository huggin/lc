class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if m != n:
            return False
        a = []
        cnt = [0] * 26
        for i in range(n):
            cnt[ord(s[i]) - ord("a")] += 1
            if s[i] != goal[i]:
                a.append(i)

        if len(a) == 2 and s[a[0]] == goal[a[1]] and s[a[1]] == goal[a[0]]:
            return True

        if len(a) == 0 and max(cnt) >= 2:
            return True

        return False
