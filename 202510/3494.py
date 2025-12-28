class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        ans = [0] * n
        for i in range(m):
            curr = 0
            for j in range(n):
                curr = max(curr, ans[j]) + skill[j] * mana[i]
            ans[n-1] = curr
            for j in range(n-2, -1, -1):
                ans[j] = ans[j+1] - skill[j+1] * mana[i]
        
        return ans[n-1]

