class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = skill[0] * skill[-1]
        v = skill[0] + skill[-1]
        n = len(skill)
        for i in range(1, n // 2):
            if skill[i] + skill[-1 - i] != v:
                return -1
            ans += skill[i] * skill[-1 - i]
        return ans
