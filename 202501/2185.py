class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 if w.startswith(pref) else 0 for w in words)
