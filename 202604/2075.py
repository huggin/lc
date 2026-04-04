class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        m = [["$"] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                m[i][j] = encodedText[i * cols + j]

        ans = []
        i, j = 0, 0
        pj = 0
        while i < rows and j < cols and m[i][j] != "$":
            ans.append(m[i][j])
            i += 1
            j += 1
            if i == rows:
                i = 0
                j = pj + 1
                pj = j
        return "".join(ans).rstrip()
