class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        candidates.sort()
        ans = set()
        c = []
        d = defaultdict(int)
        for ca in candidates:
            if ca <= target and d[ca] < target:
                c.append(ca)
                d[ca] += 1
        n = len(c)
        prefix = set()

        def f(k, tot):
            if tot == target:
                ans.add(tuple(curr))
                return
            if tot > target or k == n:
                return
          
            curr.append(c[k])
            if tuple(curr) in prefix:
                curr.pop()
                f(k+1, tot)
                return
            else:
                prefix.add(tuple(curr))
            f(k+1, tot + c[k]) 
            curr.pop()
            f(k+1, tot)

        f(0, 0)
        return ans
