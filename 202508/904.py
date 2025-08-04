class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        j = 0
        ans = 0
        cnt = [0] * n
        tt = 0
        for i in range(n):
            cnt[fruits[i]] += 1
            if cnt[fruits[i]] == 1:
                tt += 1
            while tt > 2:
                cnt[fruits[j]] -= 1
                if cnt[fruits[j]] == 0:
                    tt -= 1
                j += 1
            ans = max(ans, i - j + 1)
        return ans
