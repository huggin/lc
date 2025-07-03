class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            nw = word + "".join(
                map(lambda c: chr((ord(c) - ord("a") + 1) % 26 + ord("a")), word)
            )
            word = nw

        return word[k - 1]
