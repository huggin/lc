class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        mc = [0] * 26
        for w in words2:
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord("a")] += 1
            for i in range(26):
                mc[i] = max(mc[i], cnt[i])

        for w in words1:
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord("a")] += 1
            flag = True
            for j in range(26):
                if cnt[j] < mc[j]:
                    flag = False
                    break
            if flag:
                ans.append(w)
        return ans
