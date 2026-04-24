class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r, u = 0, 0, 0
        for m in moves:
            if m == "L":
                l += 1
            elif m == "R":
                r += 1
            else:
                u += 1
        return max(l + u - r, r + u - l)
