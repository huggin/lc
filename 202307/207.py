from typing import List


class Solution:
    def dfs(self, v, marked, onStack, g):
        marked[v] = 1
        onStack[v] = 1
        for w in g[v]:
            if marked[w] == 0:
                if not self.dfs(w, marked, onStack, g):
                    return False
            elif onStack[w]:
                return False
        onStack[v] = 0
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for e in prerequisites:
            g[e[0]].append(e[1])

        marked = [0] * numCourses
        onStack = [0] * numCourses

        for i in range(numCourses):
            if marked[i] == 0:
                if not self.dfs(i, marked, onStack, g):
                    return False

        return True
