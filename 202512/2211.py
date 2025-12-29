class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        n = len(directions)
        i = 0
        while i < n and directions[i] == "L":
            i += 1
        j = n - 1
        while j >= 0 and directions[j] == "R":
            j -= 1
        return sum(1 for c in directions[i : j + 1] if c in "LR")
