class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        s = set()
        n = len(word)
        for i in range(n):
            s.add(word[i:min(i+n-numFriends+1,n)])
        a = sorted(s)
        return a[-1]
