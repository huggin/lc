class Solution:
    def compressedString(self, word: str) -> str:
        ans = []
        n = len(word)
        i = 0
        cnt = 0
        while i < n:
            for j in range(i, n):
                if word[j] == word[i]:
                    cnt += 1
                    if cnt == 9:
                        ans += str(cnt) + word[i]
                        i = j + 1
                        cnt = 0
                        break
                else:
                    ans += str(cnt) + word[i]
                    i = j
                    cnt = 0
                    break
            if cnt != 0:
                ans += str(cnt) + word[n - 1]
                break
        return "".join(ans)
