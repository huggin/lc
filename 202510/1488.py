class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        sl = SortedList()
        mp = {}
        for k, r in enumerate(rains):
            if r == 0:
                sl.add(k)
            else:
                ans[k] = -1
                if r in mp:
                    it = sl.bisect(mp[r])
                    if it == len(sl):
                        return []
                    ans[sl[it]] = r
                    sl.remove(sl[it])
                mp[r] = k
        return ans
