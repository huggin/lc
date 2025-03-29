class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        M = int(1e9 + 7)

        @cache
        def calc(a):
            i = 2
            ans = 0
            while i * i <= a:
                if a % i == 0:
                    ans += 1
                    while a % i == 0:
                        a //= i
                i += 1
            return ans if a == 1 else ans + 1

        def power(a, b):
            ans = 1
            while b:
                if b % 2 == 1:
                    ans = ans * a % M
                b >>= 1
                a = a * a % M
            return ans

        n = len(nums)
        ps = list(calc(c) for c in nums)

        cnt = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            while len(st) > 0 and ps[i] >= ps[st[-1]]:
                st.pop()
            if len(st) == 0:
                cnt[i] = n - i
            else:
                cnt[i] = st[-1] - i
            st.append(i)

        cnt2 = [1] * n
        st = []
        for i in range(n):
            while len(st) > 0 and ps[i] > ps[st[-1]]:
                st.pop()
            if len(st) == 0:
                cnt2[i] = i + 1
            else:
                cnt2[i] = i - st[-1]
            st.append(i)

        cnt3 = [0] * n
        for i in range(n):
            cnt3[i] = cnt[i] * cnt2[i]

        b = []
        for i in range(n):
            b.append((nums[i], cnt3[i]))
        b.sort(key=lambda x: -x[0])

        ans = 1
        for i in range(n):
            if k >= b[i][1]:
                ans = ans * power(b[i][0], b[i][1]) % M
                k -= b[i][1]
            else:
                ans = ans * power(b[i][0], k) % M
                break

        return ans
