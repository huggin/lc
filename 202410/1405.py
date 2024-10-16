class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cnt = [a, b, c]
        ans = []
        while True:
            if any(cnt):
                j = -1
                v = 0
                for i in range(3):
                    if len(ans) >= 2 and ans[-1] == ans[-2] and ans[-1] == chr(i + ord('a')):
                        continue
                    elif cnt[i] > v:
                        v = cnt[i]
                        j = i
                if j == -1:
                    break
                ans.append(chr(j+ord('a')))
                cnt[j] -= 1
            else:
                break
        return ''.join(ans)
