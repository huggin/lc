class Robot:

    def __init__(self, width: int, height: int):
        self.curr_dir = 0
        self.dir = ["East", "North", "West", "South"]
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.circle = (width + height - 2) * 2
        self.moved = False

    def step(self, num: int) -> None:
        if num > 0:
            self.moved = True
        num %= self.circle
        for _ in range(num):
            if not (
                0 <= self.x + self.dx[self.curr_dir] < self.width
                and 0 <= self.y + self.dy[self.curr_dir] < self.height
            ):
                self.curr_dir = (self.curr_dir + 1) % 4
            self.x += self.dx[self.curr_dir]
            self.y += self.dy[self.curr_dir]

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.x == 0 and self.y == 0:
            if self.moved:
                return "South"
            else:
                return "East"
        return self.dir[self.curr_dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
