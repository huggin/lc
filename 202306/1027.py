class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)

        cnt = [0] * 1001
        d = {}
        for i in range(n):
            cnt[nums[i]] += 1
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)

        ans = max(cnt)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    continue
                curr = j
                delta = nums[j] - nums[i]
                total = 2
                for k in range(2, n):
                    if nums[i] + k * delta in d:
                        found = False
                        for idx in d[nums[i] + k * delta]:
                            if idx > curr:
                                curr = idx
                                total += 1
                                found = True
                                break
                        if not found:
                            break
                    else:
                        break
                ans = max(ans, total)

        return ans
