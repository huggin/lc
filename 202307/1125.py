class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        skills_2_idx = {}
        for idx, skill in enumerate(req_skills):
            skills_2_idx[skill] = idx

        n = len(req_skills)
        dp = [n + 1] * (1 << n)
        last = {}
        dp[0] = 0
        for idx, p in enumerate(people):
            s = 0
            for skill in p:
                s |= 1 << skills_2_idx[skill]
            if s == 0:
                continue

            for j in range((1 << n) - 1, -1, -1):
                if dp[j | s] > dp[j] + 1:
                    dp[j | s] = dp[j] + 1
                    last[j | s] = (j, idx)

        ans = []
        curr = (1 << n) - 1
        while curr != 0:
            ans.append(last[curr][1])
            curr = last[curr][0]

        return ans
