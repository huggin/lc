class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for a in arr:
            j = a % k
            cnt[j] += 1
        if cnt[0] % 2 == 1:
            return False
        for i in range(1, k):
            if cnt[i] != cnt[k - i]:
                return False
        return True
