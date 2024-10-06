class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split()
        w2 = sentence2.split()
        n = len(w1)
        m = len(w2)

        if n == m:
            return w1 == w2

        if n < m:
            w1, w2 = w2, w1
            n, m = m, n
        
        i, j = 0, 0
        flag = False
        while i < n and j < m:
            if w1[i] == w2[j]:
                i += 1
                j += 1
            else:
                break
        
        i2 = n - 1
        j2 = m - 1
        while j2 >= j:
            if w1[i2] == w2[j2]:
                i2 -= 1
                j2 -= 1
            else:
                break
        
        return j2 < j
        

