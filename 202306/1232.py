class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        for i in range(n):
            j = (i + 1) % n
            k = (j + 1) % n
            d = coordinates[i][0] * (coordinates[j][1] - coordinates[k][1])
            d += coordinates[j][0] * (coordinates[k][1] - coordinates[i][1])
            d += coordinates[k][0] * (coordinates[i][1] - coordinates[j][1])
            if d != 0:
                return False

        return True
