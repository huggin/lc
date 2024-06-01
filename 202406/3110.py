class Solution:
    def scoreOfString(self, s: str) -> int:
        return reduce(
            operator.add, map(lambda x: abs(x[0] - x[1]), pairwise(map(ord, s)))
        )
