class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        d1 = {}
        for r in recipes:
            if r not in d1:
                cnt = len(d1)
                d1[r] = cnt
        for s in supplies:
            if s not in d1:
                cnt = len(d1)
                d1[s] = cnt
        for row in ingredients:
            for i in row:
                if i not in d1:
                    cnt = len(d1)
                    d1[i] = cnt
        n = len(d1)
        g = [[] for _ in range(n)]
        degree = [0] * n
        m = len(recipes)
        for i in range(m):
            degree[d1[recipes[i]]] = len(ingredients[i])
            for j in ingredients[i]:
                g[d1[j]].append(d1[recipes[i]])

        v = [0] * n
        q = deque()
        for s in supplies:
            q.append(d1[s])
            v[d1[s]] = 1

        while q:
            x = q.popleft()
            for y in g[x]:
                degree[y] -= 1
                if degree[y] == 0:
                    v[y] = 1
                    q.append(y)

        ans = []
        for r in recipes:
            if v[d1[r]] == 1:
                ans.append(r)
        return ans
