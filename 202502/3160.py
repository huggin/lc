class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        color = {}
        ans = [0] * n
        ball = {}
        for i in range(n):
            if queries[i][0] in ball:
                color[ball[queries[i][0]]] -= 1
                if color[ball[queries[i][0]]] == 0:
                    del color[ball[queries[i][0]]]

            ball[queries[i][0]] = queries[i][1]
            if queries[i][1] in color:
                color[queries[i][1]] += 1
            else:
                color[queries[i][1]] = 1
            ans[i] = len(color)
        return ans
