class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        rules = {}
        for a in allowed:
            key = (1 << ((ord(a[0]) - ord("A")) + 32)) | (1 << (ord(a[1]) - ord("A")))
            if key not in rules:
                rules[key] = []
            rules[key].append(ord(a[2]) - ord("A"))

        curr = [ord(a) - ord("A") for a in bottom]

        def dfs(i, curr, curr2):
            if len(curr) == 1:
                return True
            if i + 1 == len(curr):
                return dfs(0, curr2, [])
            key = (1 << curr[i] + 32) | (1 << curr[i + 1])
            if key not in rules:
                return False
            for v in rules[key]:
                curr2.append(v)
                if dfs(i + 1, curr, curr2):
                    return True
                curr2.pop()
            return False

        return dfs(0, curr, [])
