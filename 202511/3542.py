class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = []
        ans = 0
        for num in nums:
            if num == 0:
                prev = -1
                while len(st) > 0:
                    if st[-1] != prev:
                        ans += 1
                    prev = st.pop()
                continue
            prev = -1
            while len(st) > 0 and st[-1] > num:
                if st[-1] != prev:
                    ans += 1
                prev = st.pop()
            st.append(num)

        prev = -1
        while len(st) > 0:
            if st[-1] != prev:
                ans += 1
            prev = st.pop()
        return ans
