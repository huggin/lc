class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for o in operations:
            if "+" in o:
                ans += 1
            else:
                ans -= 1
        return ans
