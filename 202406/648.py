class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        s = set(dictionary)
        for k, w in enumerate(words):
            for i in range(len(w)):
                if w[0 : i + 1] in s:
                    words[k] = w[0 : i + 1]
                    break
        return " ".join(words)
