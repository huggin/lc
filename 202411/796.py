class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s + s
        for i in range(len(s) - len(goal) + 1):
            j = 0
            while j < len(goal):
                if s[i + j] != goal[j]:
                    break
                j += 1
            if j == len(goal):
                return True
        return False
