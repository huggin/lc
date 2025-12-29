from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(k):
            freq[nums[i]] += 1

        s = SortedList([(v, k) for k, v in freq.items()])
        xx = x
        total = 0
        used = set()
        for i in range(len(s) - 1, -1, -1):
            if xx > 0:
                total += s[i][0] * s[i][1]
                used.add(s[i][1])
                xx -= 1

        ans = [0] * (len(nums) - k + 1)
        ans[0] = total
        for i in range(k, len(nums)):
            if nums[i] == nums[i - k]:
                ans[i - k + 1] = total
                continue

            j = s.bisect_left((freq[nums[i - k]], nums[i - k]))
            if nums[i - k] in used:
                total -= freq[nums[i - k]] * nums[i - k]
                used.remove(nums[i - k])
            s.pop(j)
            if freq[nums[i]] > 0:
                j2 = s.bisect_left((freq[nums[i]], nums[i]))
                if nums[i] in used:
                    used.remove(nums[i])
                    total -= freq[nums[i]] * nums[i]
                s.pop(j2)

            freq[nums[i]] += 1
            s.add((freq[nums[i]], nums[i]))

            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] > 0:
                s.add((freq[nums[i - k]], nums[i - k]))
            j2 = len(s) - x
            if j2 < 0:
                total += freq[nums[i]] * nums[i] + freq[nums[i - k]] * nums[i - k]
                used.add(nums[i])
                if freq[nums[i - k]] > 0:
                    used.add(nums[i - k])
            else:
                if (freq[nums[i]], nums[i]) >= s[j2]:
                    used.add(nums[i])
                    total += freq[nums[i]] * nums[i]
                if (freq[nums[i - k]], nums[i - k]) >= s[j2]:
                    used.add(nums[i - k])
                    total += freq[nums[i - k]] * nums[i - k]

                while len(used) < x and j2 >= 0:
                    total += s[j2][0] * s[j2][1]
                    used.add(s[j2][1])
                    j2 -= 1
                if len(used) > x:
                    total -= s[j2 - 1][0] * s[j2 - 1][1]
                    used.remove(s[j2 - 1][1])

            ans[i - k + 1] = total

        return ans
