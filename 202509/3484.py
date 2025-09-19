class Spreadsheet:

    def __init__(self, rows: int):
        self.d = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.d[cell] = value

    def resetCell(self, cell: str) -> None:
        self.d[cell] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        if a[0].isdigit():
            if b[0].isdigit():
                return int(a) + int(b)
            else:
                return int(a) + self.d[b]
        else:
            if b[0].isdigit():
                return self.d[a] + int(b)
            else:
                return self.d[a] + self.d[b]


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
