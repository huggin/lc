class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)
        neg1 = sum(1 for c in nums1 if c < 0)
        neg2 = sum(1 for c in nums2 if c < 0)
        pos1 = n1 - neg1
        pos2 = n2 - neg2

        total_pos = neg1 * neg2 + pos1 * pos2
        total_neg = n1 * n2 - total_pos

        i, j = n1, n2
        for kk, v in enumerate(nums1):
            if v >= 0:
                i = kk
                break
        for kk, v in enumerate(nums2):
            if v >= 0:
                j = kk
                break

        def count(v):
            cnt = 0
            idx2 = j
            for idx in range(0, i):
                while idx2 < n2 and nums1[idx] * nums2[idx2] > v:
                    idx2 += 1
                cnt += n2 - idx2

            idx2 = i
            for idx in range(0, j):
                while idx2 < n1 and nums1[idx2] * nums2[idx] > v:
                    idx2 += 1
                cnt += n1 - idx2
            return cnt

        def count2(v):
            cnt = 0
            idx2 = n2 - 1
            for idx in range(i, n1):
                while idx2 >= j and nums1[idx] * nums2[idx2] > v:
                    idx2 -= 1
                cnt += idx2 - j + 1

            idx2 = 0
            for idx in range(i - 1, -1, -1):
                while idx2 < j and nums1[idx] * nums2[idx2] > v:
                    idx2 += 1
                cnt += j - idx2

            return cnt

        def getNeg(k):
            lo, hi = min(nums1[0] * nums2[-1], nums1[-1] * nums2[0]), 0
            ans = 0
            while lo <= hi:
                mi = (lo + hi) >> 1
                if count(mi) >= k:
                    ans = mi
                    hi = mi - 1
                else:
                    lo = mi + 1

            return ans

        def getPos(k):
            lo, hi = 0, max(nums1[0] * nums2[0], nums1[-1] * nums2[-1])
            ans = 0
            while lo <= hi:
                mi = (lo + hi) >> 1
                if count2(mi) >= k:
                    ans = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            return ans

        if total_neg >= k:
            return getNeg(k)
        else:
            return getPos(k - total_neg)
