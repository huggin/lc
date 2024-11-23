class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])

        a = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            j, k = n - 1, n - 1
            while j >= 0:
                if box[i][j] == "*":
                    a[i][j] = "*"
                    while k > j:
                        a[i][k] = "."
                        k -= 1
                    j -= 1
                    k = j
                elif box[i][j] == "#":
                    a[i][k] = "#"
                    k -= 1
                    j -= 1
                else:
                    j -= 1
            while k >= 0:
                a[i][k] = "."
                k -= 1

        return list((zip(*reversed(a))))
