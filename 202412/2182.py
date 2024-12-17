class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        ans = []
        j = 25
        while j >= 0:
            if cnt[j] == 0:
                j -= 1
            elif cnt[j] > repeatLimit:
                ans.extend([chr(j + ord("a"))] * repeatLimit)
                cnt[j] -= repeatLimit
                k = j - 1
                while k >= 0:
                    if cnt[k] > 0:
                        ans.append(chr(k + ord("a")))
                        cnt[k] -= 1
                        break
                    k -= 1
                if k < 0:
                    break
            else:
                ans.extend([chr(j + ord("a"))] * cnt[j])
                j -= 1

        return "".join(ans)
