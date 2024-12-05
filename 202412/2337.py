class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = 0, 0
        n = len(start)
        while i < n and j < n:
            if start[i] == target[j]:
                if start[i] == "L" and i < j or start[i] == "R" and i > j:
                    return False
                i += 1
                j += 1
            elif start[i] != "_" and target[j] != "_":
                return False
            elif start[i] == "_":
                i += 1
            else:
                j += 1

        while i < n:
            if start[i] != "_":
                return False
            i += 1
        while j < n:
            if target[j] != "_":
                return False
            j += 1

        return True
