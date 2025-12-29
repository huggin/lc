class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        MOD = 10**9 + 7
        cnt = corridor.count("S")
        if cnt % 2 == 1 or cnt < 2:
            return 0
        if cnt == 2:
            return 1

        ans = 1
        done = 0
        i = 0
        j, k = -1, -1
        while i < n:
            if corridor[i] == "S":
                done += 1
                if done == 2:
                    j = i
                if done == 3:
                    k = i
                    done = 1
                    ans = ans * (k - j) % MOD
            i += 1
        return ans
